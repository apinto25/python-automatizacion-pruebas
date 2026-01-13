import requests

BASE_URL = "http://127.0.0.1:8000"


def test_create_user():
    new_user = {
        "username": "tester_pro",
        "email": "tester@example.com"
    }

    response = requests.post(f"{BASE_URL}/users", json=new_user)
    data_created_user = response.json()

    assert response.status_code == 201
    assert data_created_user["user"]["username"] == new_user["username"]

    created_user_id = data_created_user["user"]["id"]
    assert created_user_id is not None

    response_get_user = requests.get(f"{BASE_URL}/users/{created_user_id}")
    data_get_user = response.json()

    assert response_get_user.status_code == 200
    assert data_get_user["user"]["username"] == new_user["username"]

    response_delete = requests.delete(f"{BASE_URL}/users/{created_user_id}")
    assert response_delete.status_code == 200
