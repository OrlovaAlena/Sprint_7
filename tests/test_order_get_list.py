import allure
import requests


from src.config import url


class TestGetOrders:

    @allure.title('Получение списка заказов')
    def test_get_all_orders(self):
        response = requests.get(f'{url}/api/v1/orders')
        assert response.status_code == 200
        assert response.json()['orders'][0]['courierId'] is None

    @allure.title('Получение списка заказов, доступных рядом с выбранными станциями метро')
    def test_get_orders_near_metro_stations(self):
        response = requests.get(f'{url}/api/v1/orders?nearestStation=["1", "2"]')
        assert response.status_code == 200
        assert response.json()['availableStations'][0]['name'] == 'Бульвар Рокоссовского'
        assert response.json()['availableStations'][1]['name'] == 'Черкизовская'

    @allure.title('Получение списка из десяти заказов')
    def test_get_ten_orders(self):
        response = requests.get(f'{url}/api/v1/orders?limit=10&page=0')
        assert response.status_code == 200
        assert len(response.json()['orders']) == 10

    @allure.title('Получение списка из десяти заказов, доступных рядом с выбранной станциуй метро')
    def test_get_ten_orders_near_metro_station(self):
        response = requests.get(f'{url}/api/v1/orders?limit=10&page=0&nearestStation=["110"]')
        assert response.status_code == 200
        assert len(response.json()['orders']) == 10
        assert response.json()['availableStations'][0]['name'] == 'Калужская'

    @allure.title('Получение списка заказов по несуществующему id курьера')
    def test_get_orders_with_non_exist_courier_id(self):
        courier_id = 1
        response = requests.get(f'{url}/api/v1/orders?courierId={courier_id}')
        assert response.status_code == 404
        assert response.json()['message'] == f"Курьер с идентификатором {courier_id} не найден"
