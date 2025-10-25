import requests
from utils.config import API_URL

def test_api_popular_movies():
    response = requests.get(f"{API_URL}/movie/popular")
    assert response.status_code == 200, "Expected status 200"
    data = response.json()
    assert "results" in data, "Missing results field"
    assert isinstance(data["results"], list)

