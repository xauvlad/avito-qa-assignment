import pytest
import requests
from jsonschema import validate

from api import get_item_by_seller_id
from schemas import get_item_schema, error_schema


@pytest.fixture()
def seller_id():
    return 147329

#1----
#Проверка соответствия схемы успешного ответа от запроса GET /{seller_id}/item
def test_get_item_by_seller_id_valid_schema(host_url, seller_id):
    response = get_item_by_seller_id(host_url, seller_id).json()
    validate(response, get_item_schema)

#2----
#Проврека соответствия схемы ошибки от запроса GET /{seller_id}/item
@pytest.mark.parametrize(
        "id",
        [
            "non-id!",
            -10,
            None
        ]
)    
def test_get_item_by_seller_id_invalid_schema(host_url, id):
    response = get_item_by_seller_id(host_url, id)
    validate(response.json(), error_schema)

#3----
#Проверка статуса ответа от запроса GET /{seller_id}/item
def test_get_item_by_valid_seller_id(host_url, seller_id):
    response = get_item_by_seller_id(host_url, seller_id)
    assert response.status_code == 200

#4----
#Проверка результата запроса GET /{seller_id}/item при отсутствии товаров у продавца
def test_get_item_by_seller_id_no_items(host_url):
    response = get_item_by_seller_id(host_url, 147326)
    assert response.json() == []

#5----
#Проверка статуса ответа от запроса GET /{seller_id}/item при некорректном id
@pytest.mark.parametrize(
        "id", 
        [
            "non-id!",
            -10,
            None
        ]
)
def test_get_item_by_invalid_seller_id(host_url, id):
    response = get_item_by_seller_id(host_url, id)
    assert response.status_code == 400

#6----
#Проверка статуса ответа от запроса POST /{seller_id}/item
def test_get_item_by_seller_id_invalid_method(host_url, seller_id):
    response = requests.post(f"{host_url}/api/1/{seller_id}/item")
    assert response.status_code == 405