import pytest 
import API
import helpers
import allure


class TestCreateCourier: 
    @allure.title('Успешное создание курьера')
    @allure.description('Проверка, что курьера можно создать')
    def test_create_courier(self, courier_account):
         response = API.create_courier(courier_account)

         assert response.status_code == 201
         assert response.json() == {'ok': True}

    @allure.title('Создание двух одинаковых курьеров')
    @allure.description('Проверка, что система вернет ошибку, если зарегестрировать двух одиноковых курьеров')
    def test_create_two_couriers_failed(self, courier_account): 
         response_one = API.create_courier(courier_account)
         assert response_one.status_code == 201

         response_two = API.create_courier(courier_account)
         assert response_two.status_code == 409 
         assert response_two.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Создание курьера с пустым обязательным полем')
    @allure.description('Проверка, что система вернет ошибку, если передать пустое поле login или password')
    @pytest.mark.parametrize('courier_account', [
    {
        'firstName': helpers.register_new_courier_and_return_login_password()['firstName'],
        'password': helpers.register_new_courier_and_return_login_password()['password']
    },
    {
        'login': helpers.register_new_courier_and_return_login_password()['login'],
        'firstName': helpers.register_new_courier_and_return_login_password()['firstName']
    }
    ])
    def test_create_courier_without_pass_or_login(self, courier_account): 
         response = API.create_courier(courier_account)

         assert response.status_code == 400 
         assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'
         
