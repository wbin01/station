from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# ImageField -> pip install Pillow
# https://github.com/un1t/django-resized
from django_resized import ResizedImageField  # pip: Pillow, django-resized


class ModelProduct(models.Model):
    """Store product model"""
    available_quantity = models.IntegerField(
        blank=False, null=False)
    available_quantity_is_displayed = models.BooleanField(
        default=True, blank=False, null=False)
    description = models.TextField(
        default='...', blank=True, null=True)
    discount = models.IntegerField(
        blank=True, null=True)
    discount_is_displayed = models.BooleanField(
        default=True, blank=False, null=False)
    divided_times = models.IntegerField(
        blank=False, null=False)
    divided_times_interest = models.IntegerField(
        blank=False, null=False)
    divided_times_unit = models.FloatField(
        blank=False, null=False)
    image_1 = ResizedImageField(
        size=[500, 500], crop=['middle', 'center'],
        upload_to='img_store_product/', blank=False, null=False)
    image_2 = ResizedImageField(
        size=[500, 500], crop=['middle', 'center'],
        upload_to='img_store_product/', blank=True, null=True)
    image_3 = ResizedImageField(
        size=[500, 500], crop=['middle', 'center'],
        upload_to='img_store_product/', blank=True, null=True)
    image_4 = ResizedImageField(
        size=[500, 500], crop=['middle', 'center'],
        upload_to='img_store_product/', blank=True, null=True)
    image_5 = ResizedImageField(
        size=[500, 500], crop=['middle', 'center'],
        upload_to='img_store_product/', blank=True, null=True)
    is_published = models.BooleanField(
        default=False, blank=False, null=False)
    max_quantity_per_sale = models.IntegerField(
        blank=False, null=False)
    old_price = models.FloatField(
        blank=False, null=False)
    price = models.FloatField(
        blank=False, null=False)
    registry_date = models.DateTimeField(
        default=timezone.now, blank=True)
    shipping = models.FloatField(
        blank=False, null=False)
    summary = models.CharField(
        max_length=100, default='', blank=True, null=True)
    tags = models.CharField(
        max_length=100, blank=False, null=False)
    title = models.CharField(
        max_length=200, blank=False, null=False)
    url_text = models.CharField(
        max_length=200, blank=False, null=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.title
