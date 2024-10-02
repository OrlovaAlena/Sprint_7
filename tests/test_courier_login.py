import allure
import requests

from src.helper import generate_random_string


class TestLoginCourier:

    url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'

    @allure.title('Логин курьера')
    def test_success_login_courier(self, create_new_courier):
        payload = {
            "login": create_new_courier[0],
            "password": create_new_courier[1]
        }
        response = requests.post(self.url, data=payload)
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Логин курьера без пароля')
    def test_login_without_password(self, create_new_courier):
        payload = {
            "login": create_new_courier[0],
            "password": ''
        }
        response = requests.post(self.url, data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Логин несуществующего курьера')
    def test_login_non_exist_courier(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(self.url, data=payload)
        assert response.status_code == 404
        assert response.json()['message'] == "Учетная запись не найдена"
