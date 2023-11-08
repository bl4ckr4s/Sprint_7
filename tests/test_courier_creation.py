import allure
import requests


class TestCourierCreation:
    @allure.title('Successful courier creation')
    def test_courier_creation_success(self, prepare_user_data):
        payload = prepare_user_data
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Courier creation with empty password field')
    def test_courier_creation_with_empty_field(self):
        payload = {
            'login': 'test_courier',
            'password': '',
            'firstName': 'first_name'
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 400 and response.json()['message'] == "Недостаточно данных для создания учетной записи"

    @allure.title('Error check when creating two identical couriers')
    def test_two_identical_couriers_creation_error(self, register_new_courier):
        login, password, first_name = register_new_courier
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response.status_code == 409 and response.json()['message'] == "Этот логин уже используется. Попробуйте другой."
