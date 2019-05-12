from django.db import models


class Blog(models.Model):
    contents = models.CharField(max_length=1000)
    summary = models.CharField(max_length=200)
