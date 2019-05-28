from django.db import models

import datetime

class User(models.Model):
	name = models.CharField(max_length=50,blank=False)
	birth_date = models.DateField(blank=False)
	username = models.SlugField(max_length=30, primary_key=True)
	email = models.EmailField(blank=False)

	def __str__(self):
		return str(self.name) + ":" + str(self.email)

	def age(self):
		return datetime.date.today().year - self.birth_date.year
