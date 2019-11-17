from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class TodoItem(models.Model):
    content = models.TextField()


class Team(models.Model):
    name = models.TextField(null=True)
    money = models.IntegerField(default=0)


class CustomUser(AbstractUser):
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
