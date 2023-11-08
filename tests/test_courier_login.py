import allure
import requests


class TestCourierLogin:
    @allure.title('Successful login')
    def test_courier_login_success(self, register_new_courier):
        login, password, first_name = register_new_courier
        payload = {
            "login": login,
            "password": password,
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Login with empty password field')
    def test_courier_login_with_empty_field(self):
        payload = {
            "login": "test_login",
            "password": "",
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 400 and response.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Login with invalid user')
    def test_courier_login_with_invalid_user(self):
        payload = {
            "login": "invalid_user",
            "password": "1234",
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 404 and response.json()['message'] == "Учетная запись не найдена"
