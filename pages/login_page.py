from utils.logger import get_logger
from locators.login_locator import LoginLocator
from playwright.sync_api import Page
from playwright.sync_api import expect
import time
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()

    def login(self, username, OTP1, OTP2, OTP3, OTP4, OTP5, OTP6):
        self.logger.info(f"Entering user name: {username}")
        self.page.fill(LoginLocator.USERNAME, username)
        self.logger.info("Clicking continue button")
        self.page.click(LoginLocator.CONTINUE)
        self.logger.info(f"Entering OTP1 value {OTP1}")
        self.page.fill(LoginLocator.OTP1, OTP1)
        self.logger.info(f"Entering OTP2 value {OTP2}")
        self.page.fill(LoginLocator.OTP2, OTP2)
        self.logger.info(f"Entering OTP3 value {OTP3}")
        self.page.fill(LoginLocator.OTP3, OTP3)
        self.logger.info(f"Entering OTP4 value {OTP4}")
        self.page.fill(LoginLocator.OTP4, OTP4)
        self.logger.info(f"Entering OTP5 value {OTP5}")
        self.page.fill(LoginLocator.OTP5, OTP5)
        self.logger.info(f"Entering OTP6 value {OTP6}")
        self.page.fill(LoginLocator.OTP6, OTP6)
        self.page.click(LoginLocator.VERIFY)
 
    def verify_login_message(self):
        self.logger.info("Verifying login message")
        expect(self.page.locator(LoginLocator.LOFINSUCCESSFULL)).to_have_text("Login successful")
    
    def empty_username(self, Emptyusername):
        self.page.fill(LoginLocator.USERNAME, Emptyusername)
        self.page.click(LoginLocator.CONTINUE)

    def verify_email_required_error(self):
        expect(self.page.locator(LoginLocator.EMAILREQUIRED)).to_have_text("Email is required")

    def verify_invalid_email(self, INVALIDEMAIL):
        self.page.fill(LoginLocator.USERNAME, INVALIDEMAIL)
        self.page.click(LoginLocator.CONTINUE)

    def verify_business_not_found_email(self):
        expect(self.page.locator(LoginLocator.BUISNESSNOTFOUND)).to_have_text("Business not found")

    def invalid_OTP(self, username, invalid_OTP, OTP2, OTP3, OTP4, OTP5, OTP6):
        self.page.fill(LoginLocator.USERNAME, username)
        self.page.click(LoginLocator.CONTINUE)
        self.page.fill(LoginLocator.OTP1, invalid_OTP)
        self.page.fill(LoginLocator.OTP2, OTP2)
        self.page.fill(LoginLocator.OTP3, OTP3)
        self.page.fill(LoginLocator.OTP4, OTP4)
        self.page.fill(LoginLocator.OTP5, OTP5)
        self.page.fill(LoginLocator.OTP6, OTP6)
        self.page.click(LoginLocator.VERIFY)
    
    def verify_invalid_otp_error_message(self):
        expect(self.page.locator(LoginLocator.INVALIDOTPERROR)).to_have_text("Invalid OTP")
