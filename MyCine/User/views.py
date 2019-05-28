from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


from .models import User
from .serializers import UserSerializer
from Movie.models import Movie
from Movie.serializers import MovieSerializer

def get_user(username):
	try:
		return User.objects.get(pk=username)
	except User.DoesNotExist:
		raise Http404

class UserAdd(APIView):
	"""
	Add a new User
	"""
	def post(self,request):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
	"""
	Give detail of particular User and allow to edit it
	"""

	def get(self, request, username):
		user = get_user(username)
		serializer = UserSerializer(user)
		return Response(serializer.data)

	def put(self, request, username):
		user = get_user(username)
		request.data.pop('username') # Don't Allow Username to be updated
		serializer = UserSerializer(user, data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, username):
		user = self.get_user(username)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	
	
