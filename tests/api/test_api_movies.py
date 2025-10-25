import pytest
import requests
from utils.config import TRENDING_API

@pytest.mark.api
def test_trending_api_response_status(setup_logging):
    logger = setup_logging
    logger.info("Validating Trending API status")
    response = requests.get(TRENDING_API)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

@pytest.mark.api
def test_trending_api_content(setup_logging):
    logger = setup_logging
    logger.info("Validating Trending API response content")
    response = requests.get(TRENDING_API)
    data = response.json()
    assert "results" in data, "Key 'results' missing in API response"
    assert len(data["results"]) > 0, "No trending movies/TV shows found"
