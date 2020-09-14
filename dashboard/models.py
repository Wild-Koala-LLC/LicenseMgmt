from django.db import models

# Create your models here.

class License(models.Model):
	name = models.CharField(max_length=200)
	key = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date added')
	start_date = models.DateTimeField('start date')
	end_date = models.DateTimeField('end date')
	licenses_remaining = models.IntegerField()
	
