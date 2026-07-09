from playwright.sync_api import Page


class OpeningPage:

    def __init__(self, page: Page):
        self.page = page

    # ==========================================================
    # Read all Forms from Opening Page
    # ==========================================================

    def get_forms(self):

        print("\nReading Forms...")

        forms = []

        rows = self.page.locator(
            "tr:has(a[href*='ComReport.jsp'])"
        )

        total = rows.count()

        print(f"Found {total} report rows.\n")

        for i in range(total):

            row = rows.nth(i)

            try:

                name = row.locator(
                    "td.ff"
                ).first.inner_text()

                name = " ".join(name.split())

                has_individual = (
                    row.locator(
                        "a[href*='IndReport.jsp']"
                    ).count() > 0
                )

                forms.append({

                    "row": i,
                    "name": name,
                    "has_individual": has_individual

                })

                print(f"{i+1}. {name}")

            except Exception as e:

                print(f"Skipped row {i}: {e}")

        return forms

    # ==========================================================
    # Open Tenderer's Hash Page
    # ==========================================================

    def open_hash_page(self):

        print("\nOpening Tenderer's Hash...")

        self.page.locator(

            "a[href*='ViewTendererHash.jsp']"

        ).click()

        self.page.wait_for_load_state("networkidle")

        print("Opened.")

    # ==========================================================
    # Read Tenderers
    # ==========================================================

    def get_tenderers(self):

        print("\nReading Tenderers...")

        tenderers = []

        tables = self.page.locator("table.tableList_1")

        target = None

        for i in range(tables.count()):

            table = tables.nth(i)

            header = " ".join(

                table.locator("th").all_inner_texts()

            )

            if "Tenderers / Consultants" in header:

                target = table

                break

        if target is None:

            raise Exception(

                "Tenderers table not found."

            )

        rows = target.locator("tbody > tr")

        for i in range(1, rows.count()):

            cols = rows.nth(i).locator("td")

            if cols.count() < 2:
                continue

            name = cols.nth(1).inner_text()

            name = " ".join(name.split())

            tenderers.append(name)

            print(name)

        return tenderers

    # ==========================================================
    # Return to Opening Page
    # ==========================================================

    def back_to_opening(self):

        print("\nReturning to Opening page...")

        self.page.locator(

            "a.action-button-goback"

        ).click()

        self.page.wait_for_load_state("networkidle")

        print("Returned.")

    # ==========================================================
    # Open Individual Report
    # ==========================================================

    def open_individual_report(self, form):

        print(f"\nOpening {form['name']}")

        rows = self.page.locator(

            "tr:has(a[href*='ComReport.jsp'])"

        )

        row = rows.nth(form["row"])

        link = row.locator(

            "a[href*='IndReport.jsp']"

        )

        if link.count() == 0:

            raise Exception(

                "Individual Report not found."

            )

        link.first.click()

        self.page.wait_for_load_state(

            "networkidle"

        )

        print("Opened.")

    # ==========================================================
    # Open Comparative Report
    # ==========================================================

    def open_comparative_report(self, form):

        print(f"\nOpening {form['name']}")

        rows = self.page.locator(

            "tr:has(a[href*='ComReport.jsp'])"

        )

        row = rows.nth(form["row"])

        row.locator(

            "a[href*='ComReport.jsp']"

        ).first.click()

        self.page.wait_for_load_state(

            "networkidle"

        )

        print("Opened.")