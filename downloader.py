from pathlib import Path
from playwright.sync_api import Page


class Downloader:

    def __init__(self, page: Page, folders):

        self.page = page
        self.folders = folders

    # ==========================================================
    # Download ALL bidder files of ONE Individual Report
    # ==========================================================

    # ==========================================================
    # Download ALL bidder files
    # ==========================================================

    def download_individual_report(self, form_name):

        bidder_tables = self.page.locator(
            "table.individualReportCsvDownload"
        )

        print(f"\nFound {bidder_tables.count()} bidders.\n")

        for i in range(bidder_tables.count()):

            bidder_table = bidder_tables.nth(i)

            bidder_name = bidder_table.locator(
                "a[href*='ViewRegistrationDetail.jsp']"
            ).inner_text().strip()

            print()
            print("=" * 70)
            print(bidder_name)

            bidder_folder = self.folders.get_bidder_folder(
                form_name,
                bidder_name
            )

            self.download_bidder_documents(
                bidder_table,
                bidder_folder
            )

        print("\nFinished downloading this report.")

    # ==========================================================
    # Download one bidder's documents
    # ==========================================================

        # ==========================================================
    # Download one bidder's documents
    # ==========================================================

    def download_bidder_documents(
        self,
        bidder_table,
        bidder_folder
    ):

        current = bidder_table.locator("xpath=following-sibling::*")

        doc_table = None

        for i in range(current.count()):

            element = current.nth(i)

            tag = element.evaluate(
                "(e)=>e.tagName.toLowerCase()"
            )

            # -----------------------------
            # Next bidder reached
            # -----------------------------
            if tag == "table":

                if element.locator(
                    "a[href*='ViewRegistrationDetail.jsp']"
                ).count() > 0:

                    break

                # -----------------------------
                # Document table
                # -----------------------------
                headers = element.locator("th").all_inner_texts()

                header_text = " ".join(headers)

                if (
                    "Mapped Document Name" in header_text
                    and
                    "File Name" in header_text
                ):

                    doc_table = element
                    break

        if doc_table is None:

            print("Files : 0")
            return

        download_links = doc_table.locator(
            "a.action-button-download"
        )

        print(f"Files : {download_links.count()}")

        for i in range(download_links.count()):

            link = download_links.nth(i)

            filename = self.get_filename(link)

            destination = bidder_folder / filename

            print(f"Downloading : {filename}")

            try:

                with self.page.expect_download() as d:

                    link.click()

                download = d.value

                download.save_as(destination)

                print("Saved.")

            except Exception as e:

                print(e)

    # ==========================================================
    # Read filename
    # ==========================================================

    def get_filename(self, link):

        href = link.get_attribute("href")

        if href is None:

            return "Unknown.pdf"

        if "fileName=" in href:

            name = href.split("fileName=")[1]

            if "&" in name:

                name = name.split("&")[0]

            from urllib.parse import unquote

            name = unquote(name)

            return self.clean_filename(name)

        return "Unknown.pdf"

    # ==========================================================
    # Clean filename
    # ==========================================================

    @staticmethod
    def clean_filename(name):

        invalid = '<>:"/\\|?*'

        for c in invalid:

            name = name.replace(c, "_")

        return name.strip()