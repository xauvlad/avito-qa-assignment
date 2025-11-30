import pytest
import random
import string
from jsonschema import validate

from api import post_item, get_item_by_id
from schemas import post_item_schema, error_schema


def random_name():
    return "".join(random.choice(string.ascii_letters) for _ in range(random.randint(4, 10)))

@pytest.fixture()
def payload():
    payload = {
        "sellerId": 147329,
        "name": random_name(),
        "price": random.randint(100, 1000),
        "statistics": {
            "likes": random.randint(0, 100),
            "viewCount": 100,
            "contacts": 10,
        }
    }
    return payload

#1----
#Проверка соответствия схемы успешного ответа от запроса POST /item
def test_post_item_valid_schema(host_url, payload):
    response = post_item(host_url, payload)
    validate(response.json(), post_item_schema)

#2----
#Проверка соответствия схемы ошибки от запроса POST /item
def test_post_item_invalid_schema(host_url):
    payload = {"invalid": "payload"}
    response = post_item(host_url, payload)
    validate(response.json(), error_schema)

#3----
#Проверка статусов ответа от запроса POST /item
def test_post_item_valid_payload(host_url, payload):
    response = post_item(host_url, payload)
    assert response.status_code == 200

#4----
#Проверка статусов ответа от запроса POST /item с невалидными данными
@pytest.mark.parametrize(
        "sellerID, name, price, statistics",
        [
            (None, None, None, None),
            (None, "LG", 1234, {"likes": 21, "viewCount": 111, "contacts": 43}),
            (14732678, "Ботинки", 3214, {"likes": 21, "viewCount": 111, "contacts": 4}),
            (-10, "Айфон", 99999, {"likes": 14, "viewCount": 130, "contacts": 4}),
            (147329, "Марля", 1234, None),
            (147329, "", 1234, {"likes": 14, "viewCount": 130, "contacts": 3}),
            (147329, -1, 1234, {"likes": 14, "viewCount": 130, "contacts": 3}),
            (147326, "Ложка", "тысяча двести тридцать четыре", {"likes": 1, "viewCount": 161, "contacts": 4}),
            (147326, "Игорь", 3214, {"likes": "ноль", "viewCount": 161, "contacts": 4})
        ]
)
def test_post_item_invalid_payload(host_url, sellerID, name, price, statistics):
    invalid_payload = {
            "sellerId": sellerID,
            "name": name,
            "price": price,
            "statistics": statistics
    }
    response = post_item(host_url, invalid_payload)
    assert response.status_code == 400

#5----
#Проверка корректности заполнения поля statistics по умолчанию
def test_post_item_empty_statistics(host_url):
    payload_no_stats = {
            "sellerId": 147329,
            "name": "Владимир",
            "price": 322,
            "statistics": {}
    }
    response = post_item(host_url, payload_no_stats)
    item_id = response.json()["status"].split(" ")[-1]
    item = get_item_by_id(host_url, item_id).json()[0]
    assert item["statistics"] == {"likes": 0, "viewCount": 0, "contacts": 0}

#6----
#Проверка корректности id нового товара
def test_post_item_correct_item_id(host_url, payload):
    #Попарный тест для проверки корректности id нового товара
    response = post_item(host_url, payload)
    item_id = response.json()["status"].split(" ")[-1]
    assert get_item_by_id(host_url, item_id).json()[0]["name"] == payload["name"]
                                  