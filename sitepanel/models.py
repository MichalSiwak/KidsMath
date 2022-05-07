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

    def get_points(self):
        return self.__points

    def set_points(self, point):
        self.points += point


class ProfileParent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
