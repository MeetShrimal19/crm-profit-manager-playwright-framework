from utils.logger import get_logger
from locators.product_locator import ProductLocator
from playwright.sync_api import Page
from playwright.sync_api import expect
import random

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
    
    def click_products(self):
        self.page.locator(ProductLocator.PRODUCTS).click()
    
    def verify_product_url(self):
        expect(self.page).to_have_url("https://dev.profitmanager.in/products")

    def click_add_product(self):
        self.page.locator(ProductLocator.ADDPRODUCT).click()

    def verify_product_page_text(self):
        expect(self.page.locator(ProductLocator.VERIFYADDPRODUCTTEXT)).to_have_text("Fill in the details to add a new product to your inventory")

    def click_product_type_dropdown(self):
            dropdown = self.page.locator(ProductLocator.SELECTPRODUCTTYPEDROPDOWN)
            dropdown.wait_for(state="visible")
            dropdown.select_option(value="Finished")

    def select_finished_product(self):
        self.page.select_option(ProductLocator.SELECTPRODUCTTYPEDROPDOWN, value="Finished")

    def fill_product_name(self):
        productname = "product_" + str(randint(999,9999))  
        self.page.locator(ProductLocator.ENTERPRODUCTNAME).fill("new product")
