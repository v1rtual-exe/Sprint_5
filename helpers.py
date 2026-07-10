from generators import generate_email, generate_password


def get_user_data():
    """Возвращает словарь с email и паролем"""
    return {
        "email": generate_email(),
        "password": generate_password()
    }