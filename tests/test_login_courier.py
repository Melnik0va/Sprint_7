import pytest 
import API
import helpers
import allure


class TestLoginCourier: 
    @allure.title('Успешная авторизация курьера')
    @allure.description('Проверка, что курьер может авторизоваться')
    def test_login_courier_success(self, created_courier_account): 
        courier_info = helpers.create_login_courier(created_courier_account)
        courier_response = API.login_courier(courier_info)

        assert courier_response.status_code == 200
        assert 'id' in courier_response.json()

    @allure.title('Авторизация с неверным логином или паролем')
    @allure.description('Проверка, что система вернет ошибку, если указать неверный логин или пароль')
    @pytest.mark.parametrize('field_to_replace', ['login', 'password'])
    def test_login_courier_incorrect_credentials(self, created_courier_account, field_to_replace):
        courier_info = helpers.create_login_courier(created_courier_account)
        courier_noname = helpers.register_new_courier_and_return_login_password()
    
        courier_info[field_to_replace] = courier_noname[field_to_replace]
        courier_response = API.login_courier(courier_info)
    
        assert courier_response.status_code == 404
        assert courier_response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Авторизация с пустым полем логина или пароля')
    @allure.description('Проверка, что система вернет ошибку, если не указать обязательные поля логина или пароля')
    @pytest.mark.parametrize('field_name', ['login', 'password'])
    def test_login_courier_with_empty_field(self, created_courier_account, field_name):
        courier_info = helpers.create_login_courier(created_courier_account)
        courier_info[field_name] = ''
    
        courier_response = API.login_courier(courier_info)

        assert courier_response.status_code == 400
        assert courier_response.json()['message'] == 'Недостаточно данных для входа'