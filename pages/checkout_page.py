from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.postal_code_input = page.locator("[data-test='postalCode']")

        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.confirmation_heading = page.locator("[data-test='complete-header']")


    def enter_shipping_details(
        self,
        first_name: str,
        last_name: str,
        postal_code: str,
    ):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_to_overview(self):
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()
