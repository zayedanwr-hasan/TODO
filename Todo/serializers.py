from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id','username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True, min_length=6)

    class Meta:
        model = User
        fields =('id','username', 'email','password') 
    
    def create(self, validate_data):
        user = User.objects.create_user(
            username=validate_data['username'],
            email=validate_data.get('email'),
            password=validate_data['password']
        )
        return user

class TodoSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields= ('id', 'owner', 'title', 'description', 'status', 'priority', 'created_at', 'updated_at')
        read_only_fields= ('id','owner','created_at','updated_at')
