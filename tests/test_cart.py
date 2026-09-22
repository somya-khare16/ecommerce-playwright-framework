from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

from utils.test_data import VALID_USER

def test_cart_contains_added_backpack(login_page: LoginPage):
    login_page.open()
    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"],
    )
    inventory_page = InventoryPage(login_page.page)
    inventory_page.add_backpack_to_cart()
    cart_page = CartPage(login_page.page)
    cart_page.open()

    expect(cart_page.backpack_name).to_be_visible()
    