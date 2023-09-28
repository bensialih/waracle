from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Cake(models.Model):
	name = models.CharField(max_length=30)
	comment = models.CharField(max_length=200)
	image_url = models.CharField(max_length=200)
	yum_factor = models.PositiveIntegerField(
		validators=[
			MaxValueValidator(5),
			MinValueValidator(1)
		],
	)
