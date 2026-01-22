def test_create_post(api_client):
    """Test creating a new post (POST)"""
    new_post_data = {
        "title": "Test Post",
        "body": "This is a test post body",
        "userId": 1
    }

    response = api_client.post('/posts', new_post_data)

    assert response.status_code == 201

    created_post = response.json()
    assert created_post['title'] == new_post_data["title"]
    assert created_post['body'] == new_post_data["body"]
    assert created_post['userId'] == new_post_data["userId"]
    assert 'id' in created_post

def test_update_post(api_client):
    """Test updating an existing post (PUT)"""
    post_id = 1
    updated_data = {
        "id": post_id,
        "title": "Updated Title",
        "body": "Updated body content",
        "userId": 1
    }

    response = api_client.put(f'/posts/{post_id}', updated_data)

    assert response.status_code == 200

    updated_post = response.json()
    assert updated_post['title'] == updated_data["title"]
    assert updated_post['body'] == updated_data["body"]

def test_delete_post(api_client):
    """Test deleting a post (DELETE)"""
    post_id = 1

    response = api_client.delete(f'/posts/{post_id}')

    assert response.status_code == 200

def test_post_lifecycle(api_client):
    """Test complete lifecycle: Read → Update → Delete"""
    # Use existing post ID (JSONPlaceholder limitation - POST returns fake IDs)
    post_id = 1

    # READ existing post
    response = api_client.get(f'/posts/{post_id}')
    assert response.status_code == 200
    original_post = response.json()
    assert 'id' in original_post
    assert 'title' in original_post

    updated_data = {
        "id": post_id,
        "title": "Updated title",
        "body": "Updated body",
        "userId": 1
    }

    response = api_client.put(f'/posts/{post_id}', updated_data)
    assert response.status_code == 200

    updated_post = response.json()

    assert updated_post['title'] == updated_data["title"]
    assert updated_post['body'] == updated_data["body"]
    assert updated_post['userId'] == updated_data["userId"]
    assert 'id' in updated_post

    response = api_client.delete(f'/posts/{post_id}')
    assert response.status_code == 200
    # Note: JSONPlaceholder fake API doesn't actually delete resources