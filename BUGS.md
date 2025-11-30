# **Bug-report**

## В процессе тестирования выявлены следующие баги:  

|№  | Тест  | Входные данные | Описание  | Серьезность | Приоритет | Статус | 
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
| 1.1 |test_get_item_by_id_invalid_schema| ```70479ed9-1111-2222-3333-a4445e26154e```  | При запросе товара по невалидному UUID поле `result.messages` <br>в ответе равно `null`, хотя по спецификации должно быть объектом. <br>Схема ответа нарушена. | Minor | Medium | Открыт |
| 1.4 |test_get_item_by_invalid_id_response| ```""```  | При запросе товара по несуществующему ID сервер возвращает `404`,<br> тогда как ожидается `400` (некорректный ID). Ошибка в статус-кодах. | Trivial | Low | Открыт |
| 2.1 |test_get_item_by_seller_id_invalid_schema| ```""```  | Ответ при невалидном sellerId не соответствует error-схеме:<br>возвращается массив вместо объекта ошибки. | Major | High | Открыт |
| 2.2 |test_get_item_by_invalid_seller_id| ```-10```  | При передаче некорректного sellerId сервер<br> возвращает массив объявлений, вместо ошибки 400. <br>Возможна уязвимость и нарушение бизнес-логики. | Minor | High | Открыт |
| 3.2 |test_get_stats_by_invalid_item_id_response| ```""```  | При запросе статистики по невалидному `itemId` <br> поле `result.messages` имеет значение `null`, что нарушает контракт. | Minor | Medium | Открыт |
| 3.4 |test_get_stats_by_item_id_invalid_schema| ```70479ed9-1111-2222-3333-a4445e26154e```  | На несуществующий ID сервер возвращает `404`, хотя ожидается `400`.<br> Несоответствие кодов ошибок. | Trivial | Low | Открыт |
| 4.1 |test_post_item_valid_schema| ```payload```  | Успешный ответ не содержит JSON с полями <br>`sellerID`, `name`, `price`, `statistics`. Сервис возвращает только строку <br>`"Сохранили объявление - <id>"`, что нарушает спецификацию. | Critical | High | Открыт |
| 4.4.1 |test_post_item_invalid_payload| ```invalid_payload```  | Сервис принимает невалидный payload (неправильные значения в statistics),<br> возвращая `200` вместо `400`. Нет валидации входных данных. | Major | High | Открыт |
| 4.4.2 |test_post_item_invalid_payload| ```invalid_payload```  | Сервис принимает отрицательный sellerId при создании объявления,<br> хотя по требованиям sellerId должен быть в диапазоне 111111–999999. | Major | High | Открыт |
| 4.5 |test_post_item_empty_statistics| ```payload_no_stats```  | При запросе созданного товара с пустыми statistics (пустой объект)<br> сервер возвращает структуру, не совместимую с ожидаемой схемой. | Major | High | Открыт |

```    
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
```

```
invalid_payload = {
    "sellerId": 14732678,
    "name": "Ботинки",
    "price": 3214,
    "statistics": {
        "likes": 21,
        "viewCount": 111,
        "contacts": 14,
    }
}
```

```
payload_no_stats = {
        "sellerId": 147329,
        "name": "Владимир",
        "price": 322,
        "statistics": {}
}
```