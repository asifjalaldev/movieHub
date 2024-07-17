
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['username']
        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

    # def update(self, instance, validated_data):
    #     instance.owner = validated_data.get('owner', instance.owner)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.created = validated_data.get('created', instance.created)
    #     return instance