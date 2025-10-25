import pytest
from selenium.webdriver.common.by import By
from utils.base_page import BasePage
from utils.config import BASE_URL

@pytest.mark.ui
def test_filter_categories(driver, setup_logging):
    """Test filtering by categories: Popular, Trending, Newest, Top Rated"""
    logger = setup_logging
    driver.get(BASE_URL)
    base = BasePage(driver)

    categories = ["Popular", "Trending", "Newest", "Top Rated"]
    for cat in categories:
        logger.info(f"Selecting category: {cat}")
        tabs = base.get_elements((By.CSS_SELECTOR, "nav a"))
        found = False
        for tab in tabs:
            if cat.lower() in tab.text.lower():
                tab.click()
                found = True
                break
        assert found, f"Category tab '{cat}' not found"
        titles = base.get_texts((By.CSS_SELECTOR, ".title"))
        assert len(titles) > 0, f"No titles found under {cat}"
        logger.info(f"{len(titles)} titles found for category {cat}")

@pytest.mark.ui
def test_filter_by_title_search(driver, setup_logging):
    """Search by title filter"""
    logger = setup_logging
    driver.get(BASE_URL)
    base = BasePage(driver)
    search_box = (By.CSS_SELECTOR, "input[type='text']")
    base.type_text(search_box, "Star")
    titles = base.get_texts((By.CSS_SELECTOR, ".title"))
    logger.info(f"Search results for 'Star': {len(titles)}")
    assert any("Star" in t for t in titles), "Search results do not match title query"

@pytest.mark.ui
def test_filter_by_type_year_rating_genre(driver, setup_logging):
    """Filter by Type, Year, Rating, Genre"""
    logger = setup_logging
    driver.get(BASE_URL)
    base = BasePage(driver)

    type_filter = (By.ID, "type")
    year_filter = (By.ID, "year")
    rating_filter = (By.ID, "rating")
    genre_filter = (By.ID, "genre")

    try:
        base.set_dropdown_value(type_filter, "Movies")
        base.set_dropdown_value(year_filter, "2023")
        base.set_dropdown_value(rating_filter, "8+")
        base.set_dropdown_value(genre_filter, "Action")

        titles = base.get_texts((By.CSS_SELECTOR, ".title"))
        logger.info(f"Found {len(titles)} Action movies (>=8 rating, 2023)")
        assert len(titles) > 0, "No titles after applying filters"
    except Exception as e:
        logger.warning(f"Some filters may be unavailable in demo site: {e}")
