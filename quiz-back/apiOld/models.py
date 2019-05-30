import json

from django.contrib.auth.models import User
from django.db import models
from django.utils.datetime_safe import datetime

class Post(models.Model):
    title = models.CharField(max_length=256)
    body = models.CharField(max_length=256)
    like_count = models.IntegerField()
    # created_at = models.DateTimeField(default=datetime.now, blank=True)
    created_by = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        obj = {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'like_count': self.like_count,
            # 'created_at': self.created_at,
        }
        return json.dumps(obj)

    def to_json(self):
        obj = {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'like_count': self.like_count,
            # 'created_at': self.created_at,
        }
        return obj