import pytest
import requests
from jsonschema import validate

from api import get_item_by_id
from schemas import get_item_schema, error_schema


#Несуществующий id (соответствует формату uuid)                                      
nonexistent_id = "70479ed9-1111-2222-3333-a4445e26154e"

#1----
#Проверка соответствия схемы успешного ответа от запроса GET /item/{id}
def test_get_item_by_id_valid_schema(host_url, item_id):
    response = get_item_by_id(host_url, item_id)
    validate(response.json(), get_item_schema)

#2----
#Проверка соответствия схемы ошибки от запроса GET /item/{id}
@pytest.mark.parametrize(
        "id",
        [
            nonexistent_id,
            "non-uuid"
        ]
)
def test_get_item_by_id_invalid_schema(host_url, id):
    response = get_item_by_id(host_url, id)
    validate(response.json(), error_schema)

#3----
#Проверка статусов ответа от запроса GET /item/{id}
def test_get_item_by_valid_id_response(host_url, item_id):
    response = get_item_by_id(host_url, item_id)
    assert response.status_code == 200

#4----
#Проверка статусов ответа от запроса GET /item/{id} с некорректными данными
@pytest.mark.parametrize(
        "id, expected",
        [             
            #строка неверного формата              
            ("non-uuid", 400),         
            #пустая строка                                                             
            ("", 400),                
            #null                          
            (None, 400),                                        
            (nonexistent_id, 404),     
        ]
)
def test_get_item_by_invalid_id_response(host_url, id, expected):
    response = get_item_by_id(host_url, id)
    assert response.status_code == expected

#5----
#Проверка статуса ответа от запроса POST /item/{id}
def test_get_item_by_id_invalid_method(host_url, item_id):
    response = requests.post(f"{host_url}/api/1/item/{item_id}")
    assert response.status_code == 405