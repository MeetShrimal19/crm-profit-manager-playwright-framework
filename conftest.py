import pytest
from core.browser_factory import BrowserFactory
from pages.login_page import LoginPage
from pages.products_page import ProductPage

@pytest.fixture()
def page():
    factory = BrowserFactory()
    browser_page = factory.launch_browser()
    yield browser_page
    factory.close_browser()

@pytest.fixture()
def login_page(page):
    return LoginPage(page)

@pytest.fixture()
def product_page(page):
    return ProductPage(page)