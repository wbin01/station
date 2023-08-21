import logging


def get_default(request) -> dict:
    return {
        'brand_name': 'Station',
        'user': request.user,
        'warning_message': None}
