import allure
import requests

from src.helper import generate_random_string


class TestCreateCourier:

    url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'

    @allure.title('Создание нового курьера')
    def test_success_create_courier(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(self.url, data=payload)
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Повторное создание существующего курьера')
    def test_create_courier_that_already_exist(self, create_new_courier):
        payload = {
            "login": create_new_courier[0],
            "password": create_new_courier[1],
            "firstName": create_new_courier[2]
        }
        create = requests.post(self.url, data=payload)
        assert create.status_code == 409
        assert 'Этот логин уже используется' in create.json()['message']

    @allure.title('Создание нового курьера с недостаточными данными')
    def test_create_courier_with_lack_of_data(self):
        login = generate_random_string(10)
        first_name = generate_random_string(10)
        payload = {
            "login": login,
            "password": '',
            "firstName": first_name
        }
        response = requests.post(self.url, data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'
