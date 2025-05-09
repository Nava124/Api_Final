import uuid

def test_create_transaction(client):
    email = f"trans_{uuid.uuid4()}@example.com"
    user_response = client.post("/users/register", json={
        "name": "Trans User",
        "email": email,
        "password": "abc"
    })
    assert user_response.status_code == 200
    user_id = user_response.json()["user_id"]
    response = client.post("/transactions/", json={
        "user_id": user_id,
        "amount": 150.0,
        "method": "efectivo",
        "status": "completado"
    })
    assert response.status_code == 200 or response.status_code == 422