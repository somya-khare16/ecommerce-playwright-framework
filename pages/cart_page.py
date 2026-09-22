from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = Page
        self.shopping_cart_link = page.locator(
            "[data-test='shopping-cart-link']"
            )
        self.backpack_name = page.get_by_text(
            "Sauce Labs Backpack",
            exact=True,
            )
        self.checkout_button = page.locator("[data-test='checkout']")

    def open(self):
        self.shopping_cart_link.click()

    def start_checkout(self):
        self.checkout_button.click()