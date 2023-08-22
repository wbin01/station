from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth

import modules.context as module_context


def store(request):
    context = module_context.get_default(request)
    context['brand_name_tab'] += ' - Store'
    return render(request, 'store.html', context)
