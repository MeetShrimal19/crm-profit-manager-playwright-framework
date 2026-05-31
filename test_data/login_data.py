import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

class LoginData:
    USERNAME = os.getenv("LOGIN_USERNAME", "your.email@example.com")
    EMPTYUSERNAME = os.getenv("LOGIN_EMPTY_USERNAME", "    ")
    OTP1 = os.getenv("LOGIN_OTP_1", "1")
    OTP2 = os.getenv("LOGIN_OTP_2", "2")
    OTP3 = os.getenv("LOGIN_OTP_3", "3")
    OTP4 = os.getenv("LOGIN_OTP_4", "4")
    OTP5 = os.getenv("LOGIN_OTP_5", "5")
    OTP6 = os.getenv("LOGIN_OTP_6", "6")
    INVALIDEMAIL = os.getenv("LOGIN_INVALID_EMAIL", "invalid.email@example.com")
    INVALIDOTP1 = os.getenv("LOGIN_OTP_1", "8")