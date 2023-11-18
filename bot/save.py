from threading import Thread
import requests
from data.config import ADDRES
from django.core.management.utils import get_random_secret_key
import requests


def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper


def save_user(message) -> int():
    post_data = {
        'username': message.from_user.id,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'password': get_random_secret_key(),
    }
    url = f'{ADDRES}api/register/signup/'
    response = requests.post(url, data=post_data)
    return response
