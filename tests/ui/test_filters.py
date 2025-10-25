import pytest
from selenium.webdriver.common.by import By
from utils.base_page import BasePage
from utils.config import BASE_URL

@pytest.mark.ui
def test_filter_by_category(driver, setup_logging):
    logger = setup_logging
    logger.info("Starting test: Filter by category - Popular")
    driver.get(BASE_URL)
    base = BasePage(driver)

    tabs = base.get_elements((By.CSS_SELECTOR, "nav a"))
    found = False
    for tab in tabs:
        if "Popular" in tab.text:
            tab.click()
            found = True
            break

    assert found, "Popular tab not found"
    titles = base.get_texts((By.CSS_SELECTOR, ".title"))
    logger.info(f"Titles found: {len(titles)}")
    assert len(titles) > 0, "No titles loaded under Popular"
