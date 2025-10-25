import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import get_logger

@pytest.fixture(scope="session")
def logger():
    return get_logger()

@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()

