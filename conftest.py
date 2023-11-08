import pytest
from helper import register_new_courier_and_return_login_password, generate_random_string, delete_courier


@pytest.fixture
def register_new_courier():
    login, password, first_name = register_new_courier_and_return_login_password()
    yield login, password, first_name
    delete_courier(login, password)


@pytest.fixture
def prepare_user_data():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    user_data = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    yield user_data
    delete_courier(login, password)
