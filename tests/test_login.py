from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

from utils.test_data import VALID_USER, INVALID_USER, INVALID_LOGIN_ERROR

def test_valid_user_can_log_in(login_page: LoginPage):

    login_page.open()
    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"],
    )

    expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_invalid_user_sees_error(login_page: LoginPage):
    login_page.open()
    login_page.login(
        INVALID_USER["username"],
        INVALID_USER["password"],
    )

    expect(login_page.error_message).to_have_text(INVALID_LOGIN_ERROR)