from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth

import store.modules.context as modules_context


def index(request):
    context = modules_context.get_default(request)
    return render(request, 'index.html', context)


def logout(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            auth.logout(request)

    return redirect('index')


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')

    context = modules_context.get_default(request)
    if request.method == 'POST':
        # If error
        # context['warning_message'] = "Warning message!"
        # return render(request, 'signin.html', context)
        return redirect('index')
    else:
        return render(request, 'signin.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')

    context = modules_context.get_default(request)
    return render(request, 'signup.html', context)
