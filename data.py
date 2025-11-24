import random 

def order_info(color=None):
    first_names = ['Юлия', 'Анна', 'Мария', 'Елена', 'Ольга']
    last_names = ['Гармай', 'Иванова', 'Петрова', 'Сидорова', 'Васильева']
    cities = ['Москва', 'Санкт‑Петербург', 'Казань', 'Новосибирск', 'Екатеринбург']
    metro = ['Павелецкая', 'Курская', 'Белорусская', 'ВДНХ', 'Сокольники']
    
    data = {
        'firstName': random.choice(first_names),
        'lastName': random.choice(last_names),
        'address': f'г.{random.choice(cities)}',
        'metroStation': random.choice(metro),
        'phone': f'+7{random.randint(900, 999)}{random.randint(1000000, 9999999)}',
        'rentTime': random.randint(1, 14),
        'deliveryDate': '2026-01-01',
        'comment': 'Тестируем'
    }
    
    if color:
        data['color'] = color
    
    return data