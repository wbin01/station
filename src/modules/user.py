from django.contrib.auth.models import User
from django.contrib import auth

import modules.generators as module_generator
import modules.validations as module_validation
import hub.models


def sign_in(request) -> str:
    email = request.POST['email']
    password = request.POST['password']

    if not User.objects.filter(email=email).exists():
        return 'Incorrect email!'
    else:
        username = User.objects.get(email=email).username
        user = auth.authenticate(request, username=username, password=password)

        if not user:
            return 'Incorrect password!'
        else:
            auth.login(request, user)
            return 'success'


def sign_up(request) -> str:
    name = request.POST['name'].strip()
    username = module_generator.username_from_name(name)
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm-password']

    space_err = module_validation.invalid_whitespace(
        [name, username, email, password, confirm_password])
    if space_err:
        return space_err

    username_err = module_validation.invalid_username(username)
    if username_err:
        return username_err

    email_err = module_validation.invalid_email(email)
    if email_err:
        return email_err

    pass_err = module_validation.invalid_password(password, confirm_password)
    if pass_err:
        return pass_err

    if User.objects.filter(username=email).exists():
        return 'User already registered!'

    if User.objects.filter(email=email).exists():
        return 'E-mail already registered!'

    user = User.objects.create_user(
        username=username, first_name=name,
        email=email, password=password)
    user.save()

    user_profile = (
        hub.models.UserProfileModel.objects.create(user=user))
    user_profile.save()

    return 'success'
