import pytest
from selenium.webdriver.common.by import By
from utils.config import BASE_URL

@pytest.mark.ui
def test_pagination_next(driver, logger):
    logger.info("Starting pagination test")
    driver.get(BASE_URL)

    next_button = driver.find_element(By.CSS_SELECTOR, ".pagination__next")
    next_button.click()
    logger.info("Clicked next page")

    movie_cards = driver.find_elements(By.CSS_SELECTOR, ".movie-card__title")
    assert len(movie_cards) > 0, "Pagination failed — no results loaded"

