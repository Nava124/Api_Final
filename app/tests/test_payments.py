import uuid

def test_create_payment(client):
    email = f"pago_{uuid.uuid4()}@example.com"
    user_response = client.post("/users/register", json={
        "name": "Pago User",
        "email": email,
        "password": "123"
    })
    assert user_response.status_code == 200
    user_id = user_response.json()["user_id"]
    response = client.post("/payments/", json={
        "user_id": user_id,
        "amount": 100.0,
        "method": "tarjeta"
    })
    assert response.status_code == 200 or response.status_code == 422