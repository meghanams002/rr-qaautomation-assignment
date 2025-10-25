import pytest
from selenium import webdriver
from utils.logger import setup_logger

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    return setup_logger()

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
