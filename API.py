import requests
import URLs
import allure

@allure.step('Отправка запроса на создание курьера')
def create_courier(data): 
    return requests.post(URLs.CREATE_COURIER, json=data)

@allure.step('Отправка запроса на удаление курьера')
def delete_courier(courier_id): 
    return requests.delete(URLs.DELETE_COURIER + str(courier_id))

@allure.step('Отправка запроса на логина курьера')
def login_courier(data): 
    return requests.post(URLs.LOGIN_COURIER, json=data)

@allure.step('Отправка запроса на создание заказа')
def create_order(data):
    return requests.post(URLs.CREATE_ORDER, json=data)

@allure.step('Отправка запроса на получение списка заказов')
def get_list_orders(): 
    return requests.get(URLs.GET_ORDERS)