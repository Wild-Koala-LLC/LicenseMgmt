from django.db import models

class Soldier(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Machine(models.Model):
	serial_number = models.CharField(max_length=200)
	assigned_to = models.ForeignKey(Soldier, on_delete=models.CASCADE, null=True, blank=True)
	
	def __str__(self):
		return self.serial_number

class License(models.Model):
	name = models.CharField(max_length=200)
	key = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date added')
	start_date = models.DateTimeField('start date')
	end_date = models.DateTimeField('end date')
	licenses_remaining = models.IntegerField()
	on_machine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.name
	
