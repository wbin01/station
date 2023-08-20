from django.shortcuts import render, redirect, get_object_or_404

import store.modules.context as modules_context


def index(request):
    context = modules_context.get_default(request)
    return render(request, 'index.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    context = modules_context.get_default(request)
    return render(request, 'login.html', context)


def signup(request):
    context = modules_context.get_default(request)
    return render(request, 'signup.html', context)
