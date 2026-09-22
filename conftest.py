# conftest.py is a special pytest file. Pytest discovers fixtures in it automatically; 
# tests do not need to import this file.
import pytest

from playwright.sync_api import Page

from pages.login_page import LoginPage

# @pytest.fixture tells pytest that the function below is reusable test setup.
@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)