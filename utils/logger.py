import logging

def get_logger(name="test_logger"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.FileHandler("logs/test.log")
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

