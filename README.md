# API Testing Framework

Automated REST API testing framework using Python, pytest, and requests library.

![API Tests](https://github.com/YOUR_USERNAME/api-testing/workflows/API%20Tests/badge.svg)

## Technologies
- Python 3.11
- pytest
- requests library
- GitHub Actions (CI/CD)

## Project Structure
```
api-testing/
├── tests/              # Test files
│   ├── conftest.py     # Fixtures
│   ├── test_users.py
│   ├── test_posts.py
│   └── test_crud.py
├── helpers/            # Helper utilities
│   └── api_client.py   # API client wrapper
└── requirements.txt
```

## Installation
```bash
pip install -r requirements.txt
```

## Running Tests
```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_users.py -v
```

## Test Coverage
- GET requests (retrieve resources)
- POST requests (create resources)
- PUT requests (update resources)
- DELETE requests (delete resources)
- Response validation
- Status code assertions
- JSON structure validation

## API Tested
JSONPlaceholder - Free fake REST API for testing
- Base URL: https://jsonplaceholder.typicode.com
- Endpoints: /users, /posts, /comments, /todos