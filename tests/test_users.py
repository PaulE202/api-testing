import pytest

@pytest.mark.parametrize("user_id, expected_name", [
    (1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch"),
])

def test_get_user(api_client, user_id, expected_name):
    """Test that we can retrieve user info"""
    response = api_client.get(f'/users/{user_id}')

    assert response.status_code == 200
    user = response.json()
    assert user['id'] == user_id
    assert user['name'] == expected_name
    assert 'email' in user