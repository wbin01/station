from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth

import store.modules.context as module_context
import store.modules.user as module_user


def index(request):
    context = module_context.get_default(request)
    return render(request, 'index.html', context)


def logout(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            auth.logout(request)

    return redirect('index')


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')

    context = module_context.get_default(request)
    if request.method == 'POST':
        sign_in_status = module_user.sign_in(request)

        if sign_in_status != 'success':
            context['warning_message'] = sign_in_status
            return render(request, 'signin.html', context)

        return redirect('index')
    else:
        return render(request, 'signin.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')

    context = module_context.get_default(request)
    return render(request, 'signup.html', context)
