from pages.products_page import ProductPage
from test_data.login_data import LoginData

def test_verify_product_page_url(login_page, product_page):
    login_page.login(LoginData.USERNAME, LoginData.OTP1, LoginData.OTP2, LoginData.OTP3, LoginData.OTP4, LoginData.OTP5, LoginData.OTP6 )
    product_page.click_products()
    product_page.verify_product_url()
    product_page.click_add_product()
    product_page.verify_product_page_text()
    product_page.click_product_type_dropdown()
    product_page.fill_product_name()
    product_page.select_category_dropdown()
    product_page.select_material_type()
    product_page.fill_cost_price()
    product_page.fill_selling_price()
    product_page.fill_stock_entry()
    product_page.calculate_profit_per_unit()
    product_page.verify_profit_percentage()
    product_page.click_add_product_button()

def test_product_name(login_page, product_page):
    login_page.login(LoginData.USERNAME, LoginData.OTP1, LoginData.OTP2, LoginData.OTP3, LoginData.OTP4, LoginData.OTP5, LoginData.OTP6 )
    product_page.click_products()
    product_page.verify_product_url()
    product_page.click_add_product()
    product_page.verify_product_page_text()
    product_page.click_product_type_dropdown()
    product_page.fill_product_name()
    product_page.select_category_dropdown()
    product_page.select_material_type()
    product_page.fill_cost_price()
    product_page.fill_selling_price()
    product_page.fill_stock_entry()
    product_page.click_add_product_button()
    product_page.verify_product_name_in_list()

