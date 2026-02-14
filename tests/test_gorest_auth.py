import requests
import time

def test_create_user_no_token(gorest_url):
    """Test that requests without token are rejected"""

    new_user = {
        "name": "Test User",
        "email": f"test{time.time()}@example.com",
        "gender": "male",
        "status": "active"
    }
    response = requests.post(gorest_url, json=new_user)
    assert response.status_code == 401

def test_create_user_invalid_token(gorest_url):
    """Test that requests with invalid token are rejected"""

    headers = {"Authorization": "Bearer invalidtoken123"}
    new_user = {
        "name": "Test User",
        "email": f"test{time.time()}@example.com",
        "gender": "male",
        "status": "active"
    }
    response = requests.post(gorest_url, json=new_user, headers=headers)
    assert response.status_code == 401

def test_create_user_with_auth(gorest_url, gorest_headers):
    """Test that creating user with auth succeeds"""

    new_user = {
        "name": "Test User",
        "email" : f"test{time.time()}@example.com",
        "gender" : "male",
        "status" : "active"
    }

    response = requests.post(gorest_url, json=new_user, headers=gorest_headers)
    assert response.status_code == 201

def test_create_user_missing_email(gorest_url, gorest_headers):
    """Test creating user without required email field"""

    incomplete_user = {
        "name": "Test User",
        "gender": "male",
        "status": "active"
    }
    
    response = requests.post(gorest_url, json=incomplete_user, headers=gorest_headers)
    errors = response.json()

    assert response.status_code == 422
    assert isinstance(errors, list)
    assert len(errors) > 0
    assert errors[0]['field'] == 'email'
    assert "can't be blank" in errors[0]['message'].lower()

def test_create_user_invalid_email(gorest_url, gorest_headers):
    """Test creating user with invalid email format"""

    invalid_email_user = {
        "name": "Test User",
        "email" : "notanemail",
        "gender": "male",
        "status": "active"
    }
    
    response = requests.post(gorest_url, json=invalid_email_user, headers=gorest_headers)
    errors = response.json()

    assert response.status_code == 422
    assert isinstance(errors, list)
    assert len(errors) > 0
    assert errors[0]['field'] == 'email'
    assert "is invalid" in errors[0]['message'].lower()

def test_create_user_invalid_gender(gorest_url, gorest_headers):
    """Test creating user with invalid gender"""
    
    invalid_gender_user = {
        "name": "Test User",
        "email" : f"test{time.time()}@example.com",
        "gender": "unknown",
        "status": "active"
    }
    
    response = requests.post(gorest_url, json=invalid_gender_user, headers=gorest_headers)
    errors = response.json()

    assert response.status_code == 422
    assert isinstance(errors, list)
    assert len(errors) > 0
    assert errors[0]['field'] == 'gender'
    assert "can't be blank, can be male of female" in errors[0]['message'].lower()

def test_create_user_duplicate_email(gorest_url, gorest_headers):
    """Test creating user with email that already exists"""

    unique_email = f"duplicate{time.time()}@test.com"

    new_user = {
        "name": "Test User",
        "email" : unique_email,
        "gender": "male",
        "status": "active"
    }
    
    first_response = requests.post(gorest_url, json=new_user, headers=gorest_headers)
    created_user = first_response.json()
    
    assert first_response.status_code == 201

    duplicate_response = requests.post(gorest_url, json=new_user, headers=gorest_headers)
    errors = duplicate_response.json()

    assert duplicate_response.status_code == 422
    assert isinstance(errors, list)
    assert len(errors) > 0
    assert errors[0]['field'] == 'email'
    assert "has already been taken" in errors[0]['message'].lower()

    user_id = created_user['id']
    requests.delete(f"{gorest_url}/{user_id}", headers=gorest_headers)

def test_get_nonexistent_user(gorest_url, gorest_headers):
    """Test getting user that doesn't exist"""

    user_id = 999999
    url = f"{gorest_url}/{user_id}"
    
    response = requests.get(url, headers=gorest_headers)
    assert response.status_code == 404

def test_update_nonexistent_user(gorest_url, gorest_headers):
    """Test updating user that doesn't exist"""

    user_id = 999999
    url = f"{gorest_url}/{user_id}"
    
    updated_user_data = {
        "name": "Test User",
        "email" : f"test{time.time()}@example.com",
        "gender": "male",
        "status": "active"
    }
    
    response = requests.put(url, json=updated_user_data, headers=gorest_headers)
    assert response.status_code == 404