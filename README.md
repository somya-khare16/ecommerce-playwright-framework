# E-Commerce Test Automation Framework

An end-to-end test automation framework built with Python, Playwright, and pytest.

The framework automates key customer journeys on [SauceDemo](https://www.saucedemo.com/) using the Page Object Model design pattern.

## Features

- Python, Playwright, and pytest
- Page Object Model (POM)
- Reusable pytest fixtures
- Centralized configuration and test data
- Positive and negative login scenarios
- Cart and checkout automation
- HTML test reports
- Screenshots and Playwright traces on test failure
- File-based logging
- Version-pinned dependencies

## Automated Test Scenarios

- Verify that the storefront loads
- Log in with valid credentials
- Verify the error message for invalid credentials
- Add Sauce Labs Backpack to the cart
- Verify the cart contains the added product
- Complete checkout and verify the order confirmation

## Project Structure

```text
ecommerce-playwright-framework/
├── pages/                 # Page Object classes
├── tests/                 # Automated test cases
├── utils/                 # Configuration, test data, and logging
├── conftest.py            # Shared pytest fixtures
├── pytest.ini             # Pytest and Playwright settings
├── requirements.txt       # Project dependencies
└── README.md
```

## Prerequisites

- Python 3.10 or later
- Git
- Visual Studio Code (recommended)

## Installation

```powershell
git clone <your-repository-url>
cd ecommerce-playwright-framework

py -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
python -m playwright install chromium
python -m playwright install firefox webkit
```

## Run Tests

Run all tests headlessly:

```powershell
python -m pytest
```

Watch tests run in a visible browser:

```powershell
python -m pytest --headed --slowmo=500
```
## Run the suite in all three browsers:

python -m pytest --browser chromium --browser firefox --browser webkit

## HTML Report

```powershell
python -m pytest --html=reports/test_report.html --self-contained-html
```

## Failure Artifacts

When a test fails, Playwright saves debugging artifacts in `test-results/`:

- Full-page screenshot
- Playwright trace file

Logs are written to:

```text
logs/test_execution.log
```

## Author

Somya Khare