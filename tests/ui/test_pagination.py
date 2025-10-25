from selenium.webdriver.common.by import By
from utils.base_page import BasePage
from utils.config import BASE_URL

def test_pagination_next_page(driver, setup_logging):
    logger = setup_logging
    logger.info("Testing pagination feature")
    driver.get(BASE_URL)
    base = BasePage(driver)

    first_titles = base.get_texts((By.CSS_SELECTOR, ".title"))
    next_button = (By.CSS_SELECTOR, ".next")

    base.click(next_button)
    second_titles = base.get_texts((By.CSS_SELECTOR, ".title"))

    logger.info(f"First page titles: {len(first_titles)}, Next page titles: {len(second_titles)}")
    assert first_titles != second_titles, "Pagination did not change results"
