from django.db import models


class Cake(models.Model):
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    yum_factor = models.PositiveIntegerField()
