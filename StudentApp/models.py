from django.db import models

# Create your models here.
class Student(models.Model):
	fname = models.CharField(max_length=100)
	lname = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	mobile = models.PositiveIntegerField()
	pfimg = models.ImageField(upload_to='images/')
	crted_date = models.DateTimeField(auto_now_add=True)
	updted_on = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.fname +" "+ self.lname
