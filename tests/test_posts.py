import pytest

@pytest.mark.parametrize("post_id", [1,2,3])

def test_posts(api_client, post_id):
    """Test that we can retrieve fields from posts"""
    response = api_client.get(f'/posts/{post_id}')

    assert response.status_code == 200
    post = response.json()
    assert 'id' in post
    assert 'userId' in post
    assert 'title' in post
    assert 'body' in post