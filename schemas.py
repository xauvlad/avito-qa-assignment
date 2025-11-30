#Схема для /api/1/item
post_item_schema = {
    "type": "object",
    "required": ["sellerID", "name", "price", "statistics"],
    "properties": {
        "sellerID": {"type": "integer"},
        "name": {"type": "string"},
        "price": {"type": "integer"},
        "statistics": {
            "type": "object",
            "required": ["likes", "viewCount", "contacts"],
            "properties": {
                "likes": {"type": "integer"},
                "viewCount": {"type": "integer"},
                "contacts": {"type": "integer"},
            },
        },
    },
}

#Схема успешного ответа на /api/1/item/{id} и /api/1/{sellerID}/item
get_item_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "required": ["id", "sellerId", "name", "price", "statistics", "createdAt"],
        "properties": {
            "id": {"type": "string"},
            "sellerId": {"type": "integer"},
            "name": {"type": "string"},
            "price": {"type": "integer"},
            "createdAt": {"type": "string"},
            "statistics": {
                "type": ["object", "null"],
                "required": ["likes", "viewCount", "contacts"],
                "properties": {
                    "likes": {"type": "integer"},
                    "viewCount": {"type": "integer"},
                    "contacts": {"type": "integer"},
                },
            },
        },
    },
}

#Схема успешного ответа /api/1/statistic/{id}
get_statistic_schema = {
    "type": "array",
    "items": {
        "type": ["object", "null"],
        "required": ["likes", "viewCount", "contacts"],
        "properties": {
            "likes": {"type": "integer"},
            "viewCount": {"type": "integer"},
            "contacts": {"type": "integer"},
        },
    },
}

#Схема ошибочных ответов (4**)
error_schema = {
    "type": "object",
    "required": ["result", "status"],
    "properties": {
        "result": {
            "type": "object",
            "required": ["message", "messages"],
            "properties": {
                "message": {"type": "string"},
                "messages": {
                    "type": "object",
                    "properties": {},
                },
            },
        },
        "status": {"type": "string"},
    },
}
