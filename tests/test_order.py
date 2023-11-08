import allure
import pytest
import requests


class TestOrder:
    @allure.title('Ordering a scooter in different colours or without giving a colour')
    @pytest.mark.parametrize(
        'color',
        [
            ['BLACK', ''],
            ['GREY', ''],
            ['GREY', 'BLACK'],
            []
        ]
    )
    def test_order_scooter_with_color(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }
        print(color)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
        print(response.text)
        assert response.status_code == 201 and 'track' in response.text
