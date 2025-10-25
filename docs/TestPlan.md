# Test Plan

## Objective
Validate filtering, pagination, and movie listing functionalities of https://tmdb-discover.surge.sh/ using UI and API tests.

## Scope
- Categories: Popular, Trending, Newest, Top Rated
- Filters: Type, Year, Rating, Genre
- Pagination
- API validation for movie endpoints

## Out of Scope
- Authentication
- Actual TMDB API data validation

## Test Levels
- UI Functional Tests (Selenium + Pytest)
- API Tests (Requests)
- Negative Tests (invalid slugs, pagination edge cases)

## Reporting
- HTML reports (pytest-html)
- Log files (logs/test.log)

