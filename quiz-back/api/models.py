import json

from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    owner = models.ForeignKey(User, models.CASCADE, related_name='contacts')

    def __str__(self):
        obj = {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
        }
        return str(obj)

    def to_json(self):
        obj = {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
        }
        return obj
