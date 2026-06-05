from pages.products_page import ProductPage
from test_data.login_data import LoginData

def test_verify_product_page_url(login_page, product_page):
    login_page.login(LoginData.USERNAME, LoginData.OTP1, LoginData.OTP2, LoginData.OTP3, LoginData.OTP4, LoginData.OTP5, LoginData.OTP6 )
    product_page.click_products()
    product_page.verify_product_url()
    product_page.click_add_product()
    product_page.verify_product_page_text()
    product_page.click_product_type_dropdown()
