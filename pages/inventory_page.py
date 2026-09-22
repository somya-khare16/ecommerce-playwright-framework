from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.backpack_add_to_cart_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.shopping_cart_badge = page.locator("[data-test='shopping-cart-badge']")

    def add_backpack_to_cart(self):
        self.backpack_add_to_cart_button.click()
    