import pytest
import os
from dotenv import load_dotenv
from helpers.api_client import APIClient

load_dotenv() 

@pytest.fixture(scope="session")
def base_url():
    """Base URL for JSONPlaceholder API"""
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def api_client(base_url):
    """API client instance"""
    return APIClient(base_url)

@pytest.fixture
def gorest_headers():
    """GoRest authentication headers"""
    token = os.getenv('GOREST_TOKEN')
    if not token:
        pytest.skip("GOREST_TOKEN not set in .env file")
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture
def gorest_url():
    """GoRest base URL"""
    return "https://gorest.co.in/public/v2/users"