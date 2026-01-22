import pytest
from helpers.api_client import APIClient

@pytest.fixture(scope="session")
def base_url():
    """Base URL for JSONPlaceholder API"""
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def api_client(base_url):
    """API client instance"""
    return APIClient(base_url)