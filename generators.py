import random
import string


def generate_email():
    """Генерирует уникальный email в формате имя_фамилия_номер_когорты_3цифры@домен"""
    first_name = "artem"
    last_name = "kinev"
    cohort = "50"
    random_digits = ''.join(random.choices(string.digits, k=3))
    domain = "@yandex.ru"
    return f"{first_name}_{last_name}_{cohort}_{random_digits}{domain}"


def generate_password():
    """Генерирует пароль длиной 6 символов (минимальная длина)"""
    return '123456'