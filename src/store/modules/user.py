from django.contrib.auth.models import User
from django.contrib import auth


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
