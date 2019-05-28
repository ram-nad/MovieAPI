from rest_framework import serializers

from .models import Movie, Rating

class MovieSerializer(serializers.ModelSerializer):
	avg_ratings = serializers.CharField(read_only=True)
	class Meta:
		model = Movie
		fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
	movie = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Movie.objects.all())
	class Meta:
		model = Rating
		fields = '__all__'
		
		
