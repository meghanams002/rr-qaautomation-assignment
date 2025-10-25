import pytest
from selenium.webdriver.common.by import By
from utils.config import BASE_URL

@pytest.mark.ui
def test_filter_by_genre(driver, logger):
    logger.info("Starting test_filter_by_genre")
    driver.get(BASE_URL)
    
    # Example: Click on Genre dropdown and select "Action"
    genre_dropdown = driver.find_element(By.XPATH, "//select[contains(@id,'genre')]")
    genre_dropdown.click()
    option = driver.find_element(By.XPATH, "//option[contains(., 'Action')]")
    option.click()
    
    logger.info("Selected Genre: Action")

    # Verify that movie cards load
    movie_cards = driver.find_elements(By.CSS_SELECTOR, ".movie-card__title")
    assert len(movie_cards) > 0, "No movie cards found after selecting genre"
    logger.info(f"{len(movie_cards)} movie cards loaded after filtering by Action genre")

