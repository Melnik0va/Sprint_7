import pytest
import API
import data
import allure

class TestCreateOrder:
    @allure.title('Создание заказа')
    @allure.description('Проверка создания заказа с указанием разным количеством цветов')
    @pytest.mark.parametrize('color', (['BLACK'], ['GREY'], ['BLACK', 'GREY'], ''))
    def test_create_order(self, color):
        order_info = data.order_info(color)
        response = API.create_order(order_info)

        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title('Список заказов')
    @allure.description('Проверка получения списка заказов')
    def test_get_count_orders(self): 
        response_count_orders = API.get_list_orders()

        assert response_count_orders.status_code == 200
        assert 'orders' in response_count_orders.json()
