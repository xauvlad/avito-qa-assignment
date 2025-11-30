import pytest
import requests


HOST_URL = "https://qa-internship.avito.com"

@pytest.fixture()
def host_url():
    return HOST_URL

@pytest.fixture()
def item_id():
    payload = {
        "sellerId": 923741,
        "name": "Phone",
        "price": 6778,
        "statistics": {
            "likes": 52,
            "viewCount": 100,
            "contacts": 10
        }
    }
    endpoint = "/api/1/item"
    response = requests.post(HOST_URL + endpoint, json=payload)
    return response.json()["status"].split()[-1]