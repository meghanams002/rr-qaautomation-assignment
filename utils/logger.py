import logging
import os

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    log_path = "logs/test.log"

    logger = logging.getLogger("TestLogger")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_path)
    console_handler = logging.StreamHandler()

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
