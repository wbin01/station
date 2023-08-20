import logging


def get_default(request) -> dict:
    logging.info(request)
    return {
        'brand_name': 'Store'}
