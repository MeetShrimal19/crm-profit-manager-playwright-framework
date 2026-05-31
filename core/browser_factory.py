from playwright.sync_api import sync_playwright
from utils.config_reader import get_browser, get_headless, get_url

class BrowserFactory:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def launch_browser(self):

        browser_name = get_browser()
        headless = get_headless()
        url = get_url()

        self.playwright = sync_playwright().start()

        self.browser = getattr(self.playwright,browser_name).launch(headless=headless)

        self.context = self.browser.new_context()

        self.page = self.context.new_page()

        self.page.goto(url)

        return self.page

    def close_browser(self):

        self.context.close()
        self.browser.close()
        self.playwright.stop()