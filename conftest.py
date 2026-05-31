import pytest
from core.browser_factory import BrowserFactory

@pytest.fixture()
def page():

    factory = BrowserFactory()

    browser_page = factory.launch_browser()

    yield browser_page

    factory.close_browser()