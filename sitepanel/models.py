from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    parent = models.BooleanField(default=True)
    email = models.EmailField(null=True, unique=False)


class Kids(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    kids_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kids_id')
    points = models.IntegerField(default=0)


class ProfileParent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# class ProfileKid(models.Model):
#     parent = models.ForeignKey(ProfileParent, on_delete=models.CASCADE)
#     kid = models.ForeignKey(User, on_delete=models.CASCADE)
#     points = models.IntegerField(default=0)
#



# ASDFqwer1234