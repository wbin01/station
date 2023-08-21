import os
from dotenv import load_dotenv

from django.urls import path

from .views import *

load_dotenv()
ADMIN_ROUTE = os.getenv('ADMIN_ROUTE')

urlpatterns = [
    path('', index, name='index'),
]
