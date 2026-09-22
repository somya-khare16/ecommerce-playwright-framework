from playwright.sync_api import expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.test_data import VALID_USER

def test_logged_in_user_can_add_backpack_to_cart(login_page: LoginPage):
    login_page.open()
    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"],
    )
    inventory_page = InventoryPage(login_page.page)
    # Login page browser tab → log in → inventory page in that same tab

    inventory_page.add_backpack_to_cart()
    expect(inventory_page.shopping_cart_badge).to_have_text("1")
    