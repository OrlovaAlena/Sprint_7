import allure
import requests


class TestDeleteCourier:

    @allure.title('Удаление курьера')
    def test_delete_courier(self, create_new_courier):
        payload = {
            "login": create_new_courier[0],
            "password": create_new_courier[1]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        courier_id = response.json()['id']

        delete_response = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')
        assert delete_response.status_code == 200
        assert delete_response.json() == {'ok': True}

    @allure.title('Удаление курьера с несуществующим id')
    def test_delete_without_id(self):
        courier_id = 0
        response = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')

        assert response.status_code == 404
        assert response.json()['message'] == "Курьера с таким id нет."
