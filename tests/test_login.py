import pytest
from utils.logger import get_logger
from test_data.login_data import LoginData
from pages.login_page import LoginPage

logger = get_logger()

@pytest.mark.positive
def test_valid_login(page):
    logger.info("Starting test_valid_login")
    login_page = LoginPage(page)
    login_page.login(LoginData.USERNAME, LoginData.OTP1, LoginData.OTP2, LoginData.OTP3, LoginData.OTP4, LoginData.OTP5, LoginData.OTP6 )
    logger.info("Completed test_valid_login")

@pytest.mark.positive
def test_verify_login_message(page):
    logger.info("Starting test_verify_login_message")
    login_page = LoginPage(page)
    login_page.login(LoginData.USERNAME, LoginData.OTP1, LoginData.OTP2, LoginData.OTP3, LoginData.OTP4, LoginData.OTP5, LoginData.OTP6 )
    login_page.verify_login_message()
    logger.info("Completed test_verify_login_message")

@pytest.mark.negative
def test_empty_username(page):
    logger.info("Starting test_empty_username")
    login_page = LoginPage(page)
    login_page.empty_username(LoginData.EMPTYUSERNAME)
    login_page.verify_email_required_error()
    logger.info("Completed test_empty_username")

@pytest.mark.negative
def test_invalid_email(page):
    logger.info("Starting test_invalid_email")
    login_page = LoginPage(page)
    login_page.verify_invalid_email(LoginData.INVALIDEMAIL)
    login_page.verify_business_not_found_email()
    logger.info("Completed test_invalid_email")

@pytest.mark.negative
def test_invalid_error_message(page):
    logger.info("Starting test_invalid_error_message")
    login_page = LoginPage(page)
    login_page.invalid_OTP(LoginData.USERNAME, LoginData.INVALIDOTP1, LoginData.OTP2, LoginData.OTP3, LoginData.OTP4, LoginData.OTP5, LoginData.OTP6)
    login_page.verify_invalid_otp_error_message()
    logger.info("Completed test_invalid_error_message")