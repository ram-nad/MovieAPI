from rest_framework import serializers

from .models import Celeb

class ActorSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(read_only=True)
	age = serializers.IntegerField(read_only=True)
	total_movies = serializers.IntegerField(read_only=True)
	best_rated_movie = serializers.FloatField(read_only=True)
	movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	def __init__(self, obj):
		if not isinstance(obj,Celeb) or not obj.is_actor():
			raise serializers.ValidationError()
		serializers.Serializer.__init__(self,obj)


class DirectorSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(read_only=True)
	age = serializers.IntegerField(read_only=True)
	total_directed_movies = serializers.IntegerField(read_only=True)
	best_directed_movie = serializers.FloatField(read_only=True)
	directed_movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	def __init__(self, obj):
		if not isinstance(obj,Celeb) or not obj.is_director():
			raise serializers.ValidationError()
		serializers.Serializer.__init__(self,obj)


class CelebSerializer(serializers.ModelSerializer):
	class Meta:
		model = Celeb
		fields = '__all__'
		
		
