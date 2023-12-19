from django.contrib import admin
from django.db import models


class birthday(models.Model):
    birthday = models.DateField()

    def __int__(self):
        return self.birthday


