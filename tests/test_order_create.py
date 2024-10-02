import json

import allure
import pytest
import requests

from src.config import url


class TestCreateOrder:

    @allure.title('Создание заказов самокатов в разных цветах')
    @pytest.mark.parametrize(
        'color', [
            ["BLACK"], ["GREY"], ["BLACK", "GREY"], [""]
        ]
    )
    def test_create_order_with_different_colors(self, color):
        data = {
            "firstName": "Naruto",
            "lastName": "Uzumaki",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [color]
        }
        payload = json.dumps(data)

        response = requests.post(f'{url}/api/v1/orders', data=payload)
        assert response.status_code == 201
        assert 'track' in response.json()
