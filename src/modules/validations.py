import string

from django.contrib.auth.models import User


def available_email(email: str) -> bool:
    for item in User.objects.all():
        if item.email == email:
            return False
    return True


def available_username(username: str) -> bool:
    for item in User.objects.all():
        if item.username == username:
            return False
    return True


def invalid_email(email: str) -> str | None:
    if not email:
        return 'Email cannot be blank'
    if '@' not in email or '.' not in email:
        return 'Invalid email!'
    if User.objects.filter(email=email).exists():
        return 'Email already exists!'
    return None


def invalid_image(image) -> str | None:
    if not image:
        return 'Image cannot be blank'
    msg_err = "Use images with 'jpg', 'png' or 'jpeg' extensions"
    if '.' not in image.name:
        return msg_err
    if image.name.split('.')[-1].lower() not in ['jpg', 'png', 'jpeg']:
        return msg_err
    return None


def invalid_password(password: str, confirm_password: str) -> str | None:
    if not password or password == ' ':
        return 'The password cannot be blank'

    if not confirm_password or confirm_password == ' ':
        return 'Password confirmation cannot be blank'

    if password and len(password) < 8:
        return 'Password must be 8 or more characters'

    found_lowercase_in_password = False
    for char in string.ascii_lowercase:
        if char in password:
            found_lowercase_in_password = True
            break
    if not found_lowercase_in_password:
        return 'The password must contain lowercase letters'

    found_uppercase_in_password = False
    for char in string.ascii_uppercase:
        if char in password:
            found_uppercase_in_password = True
            break
    if not found_uppercase_in_password:
        return 'The password must contain capital letters'

    found_digits_in_password = False
    for char in string.digits:
        if char in password:
            found_digits_in_password = True
            break
    if not found_digits_in_password:
        return 'The password must contain numbers'

    found_punctuation_in_password = False
    for char in string.punctuation:
        if char in password:
            found_punctuation_in_password = True
            break
    if not found_punctuation_in_password:
        return 'The password must contain special characters'

    if password != confirm_password:
        return 'Passwords do not match'

    return None


def invalid_username(username: str) -> str | None:
    if not username or username == ' ':
        return 'Username cannot be blank'

    if len(username) < 2:
        return 'Username must be 3 or more characters'

    for char in username:
        if char not in string.ascii_lowercase + string.digits:
            return f'Username cannot contain " {char} "'

    if User.objects.filter(username=username).exists():
        return 'User already registered'

    return None


def invalid_whitespace(items: list) -> str | None:
    for item in items:
        if not item or item == ' ':
            return 'No item can be a blank'
        elif item[0] == ' ':
            return 'No item can start with a blank space'
        elif item[-1] == ' ':
            return 'No item can end with a blank space'
    return None
