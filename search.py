from playwright.sync_api import Page, TimeoutError


class TenderSearch:

    def __init__(self, page: Page):

        self.page = page

    def search(self, tender_id):

        print(f"\nSearching Tender ID : {tender_id}")

        # -------------------------
        # Enter Tender ID
        # -------------------------

        self.page.wait_for_selector(
            "#txtTenderId",
            state="visible",
            timeout=10000
        )

        textbox = self.page.locator("#txtTenderId")

        textbox.fill("")

        textbox.fill(str(tender_id))

        print("Tender ID entered.")

        # -------------------------
        # Click Search
        # -------------------------

        self.page.locator("#btnSearch").click()

        print("Search button clicked.")

        # -------------------------
        # Wait until Dashboard icon appears
        # -------------------------

        self.page.wait_for_selector(
            "a[title='Dashboard']",
            timeout=10000
        )

        print("Search completed.")

    def open_dashboard(self):

        print("\nOpening Dashboard...")

        self.page.locator(
            "a[title='Dashboard']"
        ).click()

        self.page.wait_for_load_state(
            "networkidle"
        )

        print("Dashboard opened.")

    def open_opening_tab(self):

        print("\nOpening Opening Tab...")

        self.page.locator(
            "a[href*='OpenComm.jsp']"
        ).click()

        self.page.wait_for_load_state(
            "networkidle"
        )

        print("Opening page loaded.")