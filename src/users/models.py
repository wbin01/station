from django.db import models
from django.utils import timezone


class ModelUser(models.Model):
    """User model

    Fields: birth_date, email, id, name, password, registry_date, username
    """
    birth_date = models.DateTimeField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=30, blank=False, null=False)
    registry_date = models.DateTimeField(default=timezone.now, blank=True)
    username = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name
