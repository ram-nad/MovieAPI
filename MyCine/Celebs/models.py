from django.db import models

import datetime

class Celeb(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, blank=False)
	birth_date = models.DateField(blank=False)

	def __str__(self):
		return str(self.name)

	def age(self):
		return datetime.date.today().year - self.birth_date.year

	def is_director(self):
		if self.directed_movies.all().count() > 0:
			return True
		else:
			return False

	def is_actor(self):
		if self.movies.all().count() > 0:
			return True
		else:
			return False

	def total_movies(self):
		return self.movies.count()

	def total_directed_movies(self):
		return self.directed_movies.count()

	def best_rated_movie(self):
		maximum = 0
		for movie in self.movies.all():
			if maximum < movie.avg_ratings():
				maximum = movie.avg_ratings()
		return maximum

	def best_directed_movie(self):
		maximum = 0
		for movie in self.directed_movies.all():
			if maximum < movie.avg_ratings():
				maximum = movie.avg_ratings()
		return maximum
