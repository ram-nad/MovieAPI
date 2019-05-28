from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
	age = serializers.CharField(read_only=True)
	class Meta:
		model = User
		fields = '__all__'
		
