import logging

from django.contrib.auth.models import User

from hub.models import *


def default_context(request, username=None) -> dict:
    user_profile = None
    page_user_profile = None

    if UserProfileModel.objects.filter(user=request.user.id).exists():
        user_profile = UserProfileModel.objects.get(user=request.user.id)

        if not username or username == user_profile.user.username:
            page_user_profile = user_profile
        elif User.objects.filter(username=username).exists():
            page_user = User.objects.get(username=username)
            page_user_profile = UserProfileModel.objects.get(user=page_user.id)

    return {
        'brand_name': 'Station',
        'brand_name_tab': 'Station',
        'user_profile': user_profile,
        'page_user_profile': page_user_profile,
        'warning_message': None}
