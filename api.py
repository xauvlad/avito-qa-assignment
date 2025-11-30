import requests


def get_item_by_id(host_url, item_id):
    endpoint = f'/api/1/item/{item_id}'
    response = requests.get(url=f'{host_url}{endpoint}')
    return response


def get_stats_by_item_id(host_url, item_id):
    endpoint = f'/api/1/statistic/{item_id}'
    response = requests.get(url=f'{host_url}{endpoint}')
    return response


def get_item_by_seller_id(host_url, seller_id):
    endpoint = f'/api/1/{seller_id}/item'
    response = requests.get(url=f'{host_url}{endpoint}')
    return response


def post_item(host_url, payload):
    endpoint = "/api/1/item"
    response = requests.post(url=f'{host_url}{endpoint}', json=payload)
    return response