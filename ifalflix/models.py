# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

 self.name
    

class Series(models.Model):
    name = models.CharField(max_length=50)
    temp = models.IntegerField()
    trailer = models.TextField()
    description = models.TextField()
    banner = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=50)
    duration = models.FloatField()
    description = models.TextField()
    trailer = models.TextField()
    banner = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=20)


    def __str__(self):
        return self.name