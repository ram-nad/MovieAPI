from django.db import models
from django.core.exceptions import ValidationError

from Celebs.models import Celeb
from User.models import User

class Movie(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100, unique=True, blank=False)
	description = models.TextField(blank=False)
	release_date = models.DateField(blank=False)
	directors = models.ManyToManyField(Celeb,related_name='directed_movies',blank=False)
	actors = models.ManyToManyField(Celeb,related_name='movies',blank=False)

	def __str__(self):
		return str(self.title)

	def release_year(self):
		return self.release_date.year

	def avg_ratings(self):
		summation = 0
		total = 0
		for rating in self.ratings.all():
			summation += rating.rating
			total += 1
		if(total > 0):
			return summation/total
		else:
			return 0


class Rating(models.Model):
	Ratings = [
			(0.5,"0.5"),
			(1,"1"),
			(1.5,"1.5"),
			(2,"2"),
			(2.5,"2.5"),
			(3,"3"),
			(3.5,"3.5"),
			(4,"4"),
			(4.5,"4.5"),
			(5,"5"),
			(5.5,"5.5"),
			(6,"6"),
			(6.5,"6.5"),
			(7,"7"),
			(7.5,"7.5"),
			(8,"8"),
			(8.5,"8.5"),
			(9,"9"),
			(9.5,"9.5"),
			(10,"10")
		]
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="ratings")
	last_updated = models.DateTimeField(auto_now=True)
	remarks = models.TextField()
	rating = models.FloatField(blank=False,choices=Ratings)

	def __str__(self):
		return str(self.ratings)
