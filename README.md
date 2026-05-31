# 🚀 Profit Manager - Playwright Test Automation Framework

A modern, modular, and robust Playwright test automation framework written in Python using `pytest` to automate and test the Profit Manager login flows.

---

## 🛠️ Features

* **Page Object Model (POM)**: Ensures clean separation of test scripts, page objects, and element locators.
* **Environment-Driven Configuration**: Easily toggle environments, URLs, browser types, and test credentials using a `.env` file (backed up by a `config.ini` default).
* **Safe Test Teardown**: Robust browser lifecycle management to prevent dangling Playwright processes or asyncio loop exceptions.
* **Custom Logging**: Configured via `utils/logger.py` to write runtime action logs directly to `logs/automation.log`.
* **Test Categorization**: Tests are structured with `@pytest.mark.positive` and `@pytest.mark.negative` markers.

---

## 📂 Project Directory Structure

```text
Profit_manager_playwright/
│
├── config.ini                # Default browser and URL configuration
├── .env                      # Environment-specific credentials and configuration (git-ignored)
├── .gitignore                # Rules for files to exclude from git tracking
├── conftest.py               # Pytest fixtures (defines browser page setup/teardown)
├── requirements.txt          # Python dependencies
│
├── core/
│   └── browser_factory.py    # Class to launch and teardown Playwright browser contexts
│
├── locators/
│   └── login_locator.py      # Selectors and element locators for the login page
│
├── pages/
│   └── login_page.py         # Actions and assertions for the login page
│
├── test_data/
│   └── login_data.py         # Test credentials and input parameters
│
├── tests/
│   └── test_login.py         # Main suite containing positive and negative login test cases
│
└── utils/
    ├── config_reader.py      # Utility helper to load config values from .env or config.ini
    └── logger.py             # Custom logging configuration for writing to automation.log
```

---

## 💻 Getting Started

### 1. Prerequisites
Make sure you have Python 3.8+ installed on your system.

### 2. Installation
Clone the repository, navigate to the folder, and run:
```bash
# Install the required Python packages
pip install -r requirements.txt

# Download and install the Playwright browsers (chromium, firefox, webkit)
playwright install
```

### 3. Configuration Setup
Create a `.env` file at the root of the project to customize your URL, browser configurations, and login details (secrets). A default configuration is provided in the repository:

```env
# Application Configuration
APP_URL=https://dev.profitmanager.in/login

# Browser Configuration
BROWSER=chromium
HEADLESS=false

# Test Data / Credentials
LOGIN_USERNAME=shrimalmeet2001@gmail.com
LOGIN_EMPTY_USERNAME="    "
LOGIN_OTP_1=1
LOGIN_OTP_2=2
LOGIN_OTP_3=3
LOGIN_OTP_4=4
LOGIN_OTP_5=5
LOGIN_OTP_6=6
LOGIN_INVALID_EMAIL=meet@flooid.in
LOGIN_INVALID_OTP_1=8
```

---

## 🧪 Running Tests

You can run the tests using simple `pytest` commands. 

```bash
# Run all tests in verbose mode
python -m pytest -v

# Run only positive tests (e.g. valid login)
python -m pytest -m positive -v

# Run only negative tests (e.g. empty fields, invalid OTP)
python -m pytest -m negative -v

# Run in headless mode (override .env)
# Set HEADLESS=true inside .env to run without spawning browser UI.
```

---

## 📝 Test Log Reports

Whenever the test suite executes, detailed step logs are written in real-time to the log file at **`logs/automation.log`**.

Example log format:
```text
2026-05-31 23:12:30,025 - INFO - Starting test_valid_login
2026-05-31 23:12:30,026 - INFO - Entering user name: shrimalmeet2001@gmail.com
2026-05-31 23:12:30,223 - INFO - Clicking continue button
2026-05-31 23:12:30,611 - INFO - Entering OTP1 value 1
...
2026-05-31 23:12:35,521 - INFO - Completed test_valid_login
```
