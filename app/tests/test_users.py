import uuid

def test_register_user(client):
    email = f"user_{uuid.uuid4()}@example.com"
    response = client.post("/users/register", json={
        "name": "Test User",
        "email": email,
        "password": "pass123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "user_id" in data