import requests
import allure


class TestOrderList:
    @allure.title('Checks that a list of orders is returned in the response body')
    def test_order_list(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
        assert response.status_code == 200 and 'orders' in response.json()
