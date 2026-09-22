from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.test_data import CHECKOUT_DETAILS, VALID_USER

def test_user_can_complete_checkout(login_page: LoginPage):
    login_page.open()
    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"],
    )

    inventory_page = InventoryPage(login_page.page)
    inventory_page.add_backpack_to_cart()

    cart_page = CartPage(login_page.page)
    cart_page.open()
    cart_page.start_checkout()

    checkout_page = CheckoutPage(login_page.page)
    checkout_page.enter_shipping_details(
        CHECKOUT_DETAILS["first_name"],
        CHECKOUT_DETAILS["last_name"],
        CHECKOUT_DETAILS["postal_code"],
    )

    checkout_page.continue_to_overview()
    checkout_page.finish_order()

    expect(checkout_page.confirmation_heading).to_have_text(
        "Thank you for your order!"
    )