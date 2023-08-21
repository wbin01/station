from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth

import modules.context as module_context


def index(request):
    context = module_context.get_default(request)
    return render(request, 'index.html', context)
