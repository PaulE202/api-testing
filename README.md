# API Testing Framework

Automated REST API testing framework using Python, pytest, and requests library.

![API Tests](https://github.com/PaulE202/api-testing/workflows/API%20Tests/badge.svg)

## Technologies
- Python 3.13
- pytest
- requests library
- python-dotenv
- GitHub Actions (CI/CD)

## Project Structure
```
api-testing/
├── tests/
│   ├── conftest.py           # Fixtures and configuration
│   ├── test_users.py         # User endpoint tests
│   ├── test_posts.py         # Post endpoint tests
│   ├── test_crud.py          # Full CRUD lifecycle tests
│   ├── test_gorest_auth.py   # Authentication and negative test cases
├── helpers/
│   └── api_client.py         # API client wrapper
├── requirements.txt
└── .env                      # Local only - not committed
```

## Setup
```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:
```
GOREST_TOKEN=your_token_here
```
Get your GoRest token at: https://gorest.co.in/consumer/login

## Running Tests
```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_users.py -v

> **Note:** GoRest tests run locally only. GoRest blocks GitHub Actions IP ranges.
> Run `pytest tests/test_gorest_auth.py -v` locally to execute authentication and negative tests.
```

## Test Coverage

### CRUD Operations (JSONPlaceholder)
- GET requests (retrieve resources)
- POST requests (create resources)
- PUT requests (update resources)
- DELETE requests (delete resources)
- Response validation
- Status code assertions
- JSON structure validation

### Authentication & Negative Testing (GoRest)
- Valid token (201 success)
- Missing token (401 rejection)
- Invalid token (401 rejection)
- Missing required fields (422)
- Invalid field values (422)
- Duplicate email (422)
- Non-existent resources (404)
- Error message validation

## API Tested
**JSONPlaceholder** - https://jsonplaceholder.typicode.com
- Endpoints: /users, /posts

**GoRest** - https://gorest.co.in
- Endpoints: /public/v2/users
- Requires authentication (Bearer token)