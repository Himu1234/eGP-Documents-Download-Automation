# navigator.py

from playwright.sync_api import Page, TimeoutError
import selectors as sel

class Navigator:

    def __init__(self, page: Page):
        self.page = page

    def open_evaluation_committee(self):

        print("\nOpening Evaluation Committee...")

        self.page.hover(sel.MENU_EVALUATION)

        self.page.wait_for_selector(
            sel.MENU_EVALUATION_DROPDOWN,
            state="visible"
        )

        self.page.locator(
            sel.MENU_EVALUATION_COMMITTEE,
            has_text="Evaluation Committee"
        ).click()

        self.page.wait_for_load_state("networkidle")

        print("Evaluation Committee page opened.")