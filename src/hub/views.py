from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth

import modules.context as module_context


def user_profile(request, username):
    context = module_context.default_context(request, username)
    context['brand_name_tab'] += ' - Profile'

    condition_to_access = [
        context['user_profile'] and context['user_profile'].is_admin,
        username == request.user.username]

    if any(condition_to_access):
        return render(request, 'hub_user_profile.html', context)

    return redirect('index')
