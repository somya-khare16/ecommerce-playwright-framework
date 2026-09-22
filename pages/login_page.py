from playwright.sync_api import Page

from utils.config import BASE_URL
from utils.logger import get_logger

logger = get_logger(__name__)

class LoginPage:

    #__init__ runs when we create a LoginPage
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name = "Login")
        self.error_message = page.locator("[data-test='error']")
        # We place the selector in the page object so tests do not need to know the webpage’s internal HTML details.


    def open(self):
        logger.info("Opening SauceDemo login page")
        self.page.goto(BASE_URL)


    def login(self, username: str, password: str):
    # We do not log the password, because passwords should never appear in log files
        logger.info("Logging in as user: %s", username)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

