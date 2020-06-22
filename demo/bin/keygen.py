from django.utils.crypto import get_random_string


def generate_secret_key():
    """Generates a secret key for Django."""
    chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
    secret = get_random_string(50, chars)
    return secret
