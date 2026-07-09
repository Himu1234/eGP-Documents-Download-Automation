from playwright.sync_api import sync_playwright, TimeoutError
from config import LOGIN_URL, EGP_USERNAME, EGP_PASSWORD, HEADLESS


class EGPLogin:

    def __init__(self):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=HEADLESS,
            slow_mo=300
        )

        self.context = self.browser.new_context(
            accept_downloads=True
        )

        self.page = self.context.new_page()

    def login(self):

        print("=" * 60)
        print("Opening e-GP website...")
        print("=" * 60)

        self.page.goto(LOGIN_URL)

        # Wait for login page
        self.page.wait_for_selector("#txtEmailId")

        # Clear placeholder text if present
        self.page.click("#txtEmailId")
        self.page.fill("#txtEmailId", EGP_USERNAME)

        self.page.click("#txtPassword")
        self.page.fill("#txtPassword", EGP_PASSWORD)

        print("Logging in...")

        # Click Login
        self.page.click("#btnLogin")

        # Wait until page finishes loading
        self.page.wait_for_load_state("networkidle")

        print("Logged in.")
        print("Current URL:", self.page.url)

        # -------------------------------------------------------
        # Close popup if it appears
        # -------------------------------------------------------
        try:

            print("Checking for popup...")

            popup = self.page.locator("#popup_ok")

            popup.wait_for(
                state="visible",
                timeout=5000
            )

            popup.click()

            print("Popup closed successfully.")

            self.page.wait_for_timeout(1000)

        except TimeoutError:

            print("Popup did not appear.")

        except Exception as e:

            print("Unable to close popup:", e)

        # -------------------------------------------------------
        # Save authenticated session
        # -------------------------------------------------------

        try:

            self.context.storage_state(
                path="session.json"
            )

            print("Session saved as session.json")

        except Exception as e:

            print("Could not save session:", e)

        print("=" * 60)

        return self.page

    def close(self):

        self.browser.close()

        self.playwright.stop()