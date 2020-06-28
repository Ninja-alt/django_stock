from django.db import models

# Create your models here.

# database stuff
class Stock(models.Model):
	ticker = models.CharField(max_length=10)

	# admin area
	def __str__(self):
		return self.ticker