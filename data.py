import random
import string

def randomword():
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(12))

def make_user_data():
    return {
        'name': f'{randomword()}',
        'email': f'{randomword()}@yandex.ru',
        'password': f'{randomword()}'
    }
