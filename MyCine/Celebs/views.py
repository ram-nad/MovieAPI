from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import serializers

from .models import Celeb
from .serializers import CelebSerializer, DirectorSerializer, ActorSerializer

def celeb_object(id):
	try:
		return Celeb.objects.get(id=id)
	except Celeb.DoesNotExist:
		raise Http404

class DirectorDetail(APIView):
	"""
	Return a Director Details
	"""
	def get(self,request,id):
		try:
			director = DirectorSerializer(celeb_object(id))
			return Response(director.data)
		except serializers.ValidationError:
			return Response({"director":"Wrong Id"},status=status.HTTP_400_BAD_REQUEST)

class ActorDetail(APIView):
	"""
	Return a Actor Details
	"""
	def get(self,request,id):
		try:
			actor = ActorSerializer(celeb_object(id))
			return Response(actor.data)
		except serializers.ValidationError:
			return Response({"actor":"Wrong Id"},status=status.HTTP_400_BAD_REQUEST)

class CelebAdd(APIView):
	"""
	Add Celeb
	"""

	def post(self,request):
		serializer = CelebSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CelebDetail(APIView):
	"""
	Give detail of particular Celeb and allow to edit it
	"""

	def get(self, request, id):
		celeb = celeb_object(id)
		serializer = CelebSerializer(celeb)
		return Response(serializer.data)

	def put(self, request, id):
		celeb = celeb_object(id)
		serializer = CelebSerializer(celeb, data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, id):
		celeb = celeb_object(id)
		celeb.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
