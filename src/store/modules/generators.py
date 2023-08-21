import random
import string

from django.contrib.auth.models import User


def username_from_name(name: str) -> str:
    chars = string.digits + string.ascii_lowercase
    name = name.strip().replace(' ', '').lower()
    username = ''.join(x for x in name if x in chars)
    username = username + '01' if len(username) < 2 else username

    is_valid = False
    while not is_valid:
        for item in User.objects.all():
            if item.username == username:
                username += str(random.randint(10, 1000))
                continue
        is_valid = True

    return username
