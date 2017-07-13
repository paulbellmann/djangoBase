# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return "%s: %s" % (self.title, self.body)