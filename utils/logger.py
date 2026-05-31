import logging

def get_logger():

    logger = logging.getLogger("playwright_framework")

    logger.setLevel(logging.INFO)

    if not logger.handlers:

        file_handler = logging.FileHandler("logs/automation.log")

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger