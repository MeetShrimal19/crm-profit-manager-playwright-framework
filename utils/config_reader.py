import os
import configparser

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

config = configparser.ConfigParser()
config.read("config.ini")

def get_browser():
    return os.getenv("BROWSER") or config.get("browser", "browser")

def get_headless():
    val = os.getenv("HEADLESS")
    if val is not None:
        return val.lower() in ("true", "1", "yes")
    return config.getboolean("browser", "headless")

def get_url():
    return os.getenv("APP_URL") or config.get("environment", "url")