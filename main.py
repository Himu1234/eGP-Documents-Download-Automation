from login import EGPLogin
from navigator import Navigator
from search import TenderSearch
from opening import OpeningPage
from folder_manager import FolderManager
from downloader import Downloader

TENDER_ID = "1296437"


def main():

    bot = EGPLogin()

    try:

        # -------------------------------------------------
        # Login
        # -------------------------------------------------

        page = bot.login()

        # -------------------------------------------------
        # Timeout
        # -------------------------------------------------

        page.set_default_timeout(180000)
        page.set_default_navigation_timeout(180000)

        # -------------------------------------------------
        # Navigate
        # -------------------------------------------------

        navigator = Navigator(page)

        navigator.open_evaluation_committee()

        # -------------------------------------------------
        # Search Tender
        # -------------------------------------------------

        search = TenderSearch(page)

        search.search(TENDER_ID)

        search.open_dashboard()

        search.open_opening_tab()

        # -------------------------------------------------
        # Opening Page
        # -------------------------------------------------

        opening = OpeningPage(page)

        forms = opening.get_forms()

        # -------------------------------------------------
        # Read Tenderers
        # -------------------------------------------------

        opening.open_hash_page()

        opening.get_tenderers()

        opening.back_to_opening()

        # -------------------------------------------------
        # Create Folder Structure
        # -------------------------------------------------

        folders = FolderManager()

        folders.create_tender_folder(TENDER_ID)

        folders.create_form_folders(forms)

        # -------------------------------------------------
        # Open ONLY first Individual Report
        # -------------------------------------------------

        # print("\nOpening first Individual Report...\n")

        # first_form = forms[0]

        # opening.open_individual_report(first_form)

        # downloader = Downloader(page, folders)

        # downloader.download_individual_report(
        #     first_form["name"]
        # )

        # -------------------------------------------------
        # Download ALL Individual Reports
        # -------------------------------------------------

        downloader = Downloader(page, folders)

        INDIVIDUAL_FORMS = [

            "e-Tender Submission Letter (Form e-PG3 1)",

            "Tenderer Information Form (e-PG3-2) - Part 1",

            "Tenderer Information Form (e-PG3-2) - Part 2",

            "Subcontractor Information Form (Form e-PG3-3)",

            "Technical Specifications and Compliance of Goods and related services (Form e-PG3-5)"

        ]

        for form in forms:

            if form["name"] not in INDIVIDUAL_FORMS:
                continue

            print("\n" + "=" * 80)
            print(form["name"])
            print("=" * 80)

            opening.open_individual_report(form)

            downloader.download_individual_report(
                form["name"]
            )

            opening.back_to_opening()

        html = page.content()

        with open(
            "individual_report.html",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(html)

        print("\nHTML saved as:")
        print("individual_report.html")

        print("\nCurrent URL:")
        print(page.url)

        print("\nTitle:")
        print(page.title())

        print("\nPage saved successfully.")

        input("\nPress ENTER to exit...")

    finally:

        bot.close()


if __name__ == "__main__":

    main()