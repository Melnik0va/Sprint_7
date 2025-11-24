import random
import string
import API

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    login_pass = {
        'login': login,
        'password': password,
        'firstName': first_name
    }

    return login_pass

def create_login_courier(login_pass): 
         return {
              'login': login_pass['login'],
              'password': login_pass['password']
         }

def get_login_courier(login_pass):
     login_info = create_login_courier(login_pass)
     login_response = API.login_courier(login_info)
     courier_id = login_response.json().get('id')
     return courier_id

def create_courier(register=False): 
     courier_accont = register_new_courier_and_return_login_password()
     if register: 
          API.create_courier(courier_accont)
     return courier_accont

def delete_courier(login_pass):
     courier_id = get_login_courier(login_pass)
     API.delete_courier(courier_id)



