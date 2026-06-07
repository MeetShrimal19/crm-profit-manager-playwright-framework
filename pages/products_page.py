from utils.logger import get_logger
from locators.product_locator import ProductLocator
from playwright.sync_api import Page
from playwright.sync_api import expect
from random import randint 
import time
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
        self.productname = "product_" + str(randint(999,9999))  
        self.page.locator(ProductLocator.ENTERPRODUCTNAME).fill(self.productname)
    
    def select_category_dropdown(self):
        dropdown = self.page.locator(ProductLocator.CATEGORYDROPDOWN)
        dropdown.wait_for(state="visible")
        dropdown.select_option(value="2542")
    
    def select_material_type(self):
        dropdown = self.page.locator(ProductLocator.MATERIALDROPDOWN)
        dropdown.wait_for(state="visible")
        dropdown.select_option(value="2518")
    
    def fill_cost_price(self):
        self.costprice = str(randint(10,20))
        self.page.locator(ProductLocator.COSTPRICE).fill(self.costprice)

    def fill_selling_price(self):
        self.sellingprice = str(randint(21,30))
        self.page.locator(ProductLocator.SELLINGPRICE).fill(self.sellingprice)
    
    def fill_stock_entry(self):
        stockentry = str(randint(50, 70))
        self.page.locator(ProductLocator.STOCK).fill(stockentry)
    
    def click_add_product_button(self):
        self.page.locator(ProductLocator.ADDPRODUCTFORMBUTTON).click()

    def calculate_profit_per_unit(self):
        profit = int(self.sellingprice) - int(self.costprice)
        expect(self.page.locator(ProductLocator.PROFITPERUNITVALUE)).to_have_text(f"₹{profit}")
    
    def verify_profit_percentage(self):
        profit_percentage = round(
        ((int(self.sellingprice) - int(self.costprice)) / int(self.sellingprice)) * 100,1)

        expect(
            self.page.locator(ProductLocator.PROFITPERCENTAGE)
        ).to_have_text(f"{profit_percentage}% of selling price")
    
    def verify_product_name_in_list(self):
        expect(self.page.locator(ProductLocator.PRODUCTNAME).first).to_have_text(self.productname)

