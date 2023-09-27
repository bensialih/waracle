from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Cake(models.Model):
	name = models.CharField(max_length=30)
	comment = models.CharField(max_length=200)
	imageUrl = models.CharField(max_length=200)
	yumFactor = models.PositiveIntegerField(
		validators=[
			MaxValueValidator(5),
			MinValueValidator(1)
		],
	)
