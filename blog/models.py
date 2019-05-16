from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=20, default=None)
    pub_date = models.DateField(default=None)
    body = models.CharField(max_length=200, default=None)
    image = models.ImageField(upload_to='images/', default=None)
