from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# ImageField -> pip install Pillow
# https://github.com/un1t/django-resized
from django_resized import ResizedImageField  # pip: Pillow, django-resized
# https://github.com/fabiocaccamo/django-colorfield
from colorfield.fields import ColorField  # pip: django-colorfield


class StationProfileModel(models.Model):
    """Station profile model"""
    brand_image = ResizedImageField(
        size=[None, 40],  # size=[80, 40], crop=['middle', 'center'],
        upload_to='img_hub_station_profile/', blank=True, null=True)
    brand_image_in_nav_is_displayed = models.BooleanField(
        default=True, blank=False, null=False)
    brand_name = models.CharField(
        max_length=200, blank=False, null=False)
    brand_name_in_nav_is_displayed = models.BooleanField(
        default=False, blank=False, null=False)
    social_media_discord = models.CharField(
        max_length=200, blank=True, null=True)
    social_media_facebook = models.CharField(
        max_length=200, blank=True, null=True)
    social_media_github = models.CharField(
        max_length=200, blank=True, null=True)
    social_media_instagram = models.CharField(
        max_length=200, blank=True, null=True)
    social_media_linkedin = models.CharField(
        max_length=200, blank=True, null=True)
    social_media_other = models.CharField(
        max_length=200, blank=True, null=True)
    social_media_twitch = models.CharField(
        max_length=200, blank=True, null=True)
    social_media_twitter = models.CharField(
        max_length=200, blank=True, null=True)
    social_media_whatsapp = models.CharField(
        max_length=200, blank=True, null=True)
    social_media_youtube = models.CharField(
        max_length=200, blank=True, null=True)
    theme_accent_color = ColorField(
        blank=True, null=True, default='#8A42AA')
    theme_accent_color_text = ColorField(
        blank=True, null=True, default='#FFFFFF')
    theme_body_color = ColorField(
        blank=True, null=True, default='#ECECEC')
    theme_body_color_text = ColorField(
        blank=True, null=True, default='#FFFFFF')

    def __str__(self):
        return self.brand_name


class UserProfileModel(models.Model):
    """User profile model"""
    cover_image = ResizedImageField(
        size=[1000, 500], crop=['middle', 'center'],
        upload_to='img_hub_user_profile/', blank=True, null=True)
    is_admin = models.BooleanField(
        blank=False, null=False, default=False)
    is_blocked = models.BooleanField(
        blank=False, null=False, default=False)
    profile_image = ResizedImageField(
        size=[40, 40], crop=['middle', 'center'],
        upload_to='img_hub_user_profile/', blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.user.first_name
