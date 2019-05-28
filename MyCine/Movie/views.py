from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer

class MovieList(APIView):
	"""
	Show List of all Movies
	Add a new Movie
	"""

	def get(self, request):
		movies = Movie.objects.all()
		serializer = MovieSerializer(movies,many=True)
		return Response(serializer.data)

	def post(self,request):
		serializer = MovieSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	#def perform_content_negotiation(self): #This Forces to return only JSON
	#	renderers = self.get_renderers()
	#	return (renderers[0], renderers[0].media_type)


class MovieListYear(APIView):
	"""
	Show List of all Movies in a Year
	"""

	def get(self, request, year):
		if year <= 0 or year > 9999:
			return Response({"year":"Wrong Year"}, status=status.HTTP_400_BAD_REQUEST)
		movies = Movie.objects.filter(release_date__year=year)
		serializer = MovieSerializer(movies,many=True)
		return Response(serializer.data)


class MovieDetail(APIView):
	"""
	Give detail of particular movie and aloow to edit it
	"""
	def get_object(self,id):
		try:
			return Movie.objects.get(pk=id)
		except Movie.DoesNotExist:
			raise Http404

	def get(self, request, id):
		movie = self.get_object(id)
		serializer = MovieSerializer(movie)
		return Response(serializer.data)

	def put(self, request, id):
		movie = self.get_object(id)
		serializer = MovieSerializer(movie, data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, id):
		movie = self.get_object(id)
		movie.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class Rating(APIView):
	"""
	Give list of movies with higher ratings
	"""
	def get(self,request,rating):
		if(rating < 0 or rating > 10):
			return Response({"rating": "Must be between 0 to 10"},status=status.HTTP_400_BAD_REQUEST)
		movies = []
		for movie in Movie.objects.all().order_by("-release_date"):
			if movie.avg_ratings() >= rating:
				movies.append(movie)
		serializer = MovieSerializer(movies,many=True)
		return Response(serializer.data)

class RatingList(APIView):
	"""
	Show List of Ratings for a movie
	Add a new Rating for a movie
	"""

	def get(self, request, id):
		ratings = Movie.objects.get(pk=id).ratings.all()
		serializer = RatingSerializer(ratings,many=True)
		return Response(serializer.data)

	def post(self,request,id):
		request.data.update({"movie": id}) #Movie Id must be this only
		serializer = RatingSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RatingDetail(APIView):
	"""
	Detail of a Particular Rating
	Edit Rating
	"""

	def get(self, request, id, username):
		ratings = Movie.objects.get(pk=id).ratings.get(user__username=username)
		serializer = RatingSerializer(ratings)
		return Response(serializer.data)

	def put(self,request,id,username):
		request.data.update({"movie":id, "user": username}) #To prevent Overwrite
		ratings = Movie.objects.get(pk=id).ratings.get(user__username=username)
		serializer = RatingSerializer(ratings,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,id,username):
		ratings = Movie.objects.get(pk=id).ratings.get(user__username=username)
		ratings.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
