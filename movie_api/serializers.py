from rest_framework import serializers

from .models import WatchList, StreamPlatform

#  hyperlink serializers------------
class WatchListSerializer(serializers.HyperlinkedModelSerializer):
    """
    A type of `ModelSerializer` that uses hyperlinked relationships instead
    of primary key relationships. Specifically:

    * A 'url' field is included instead of the 'id' field.
    * Relationships to other instances are hyperlinks, instead of primary keys.
    """
    class Meta:
        model=WatchList
        fields='__all__'
        
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=StreamPlatform
        fields='__all__'
    

#  class base view---------------------------------

# class WatchListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=WatchList
#         fields='__all__'
        
# class StreamPlatformSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=StreamPlatform
#         fields='__all__'
    
# class WatchListSerializer(serializers.Serializer):
#     id= serializers.IntegerField(read_only=True)
#     title=serializers.CharField(max_length=50)
#     storyLine=serializers.CharField(max_length=100)
#     # platform=serializers.ForeignKey(StreamPlatform, on_delete=models.CASCADE)
#     active=serializers.BooleanField(default=True)
#     created=serializers.DateTimeField()
    
#     def create(self, validated_data):
#         """
#         create and return a new 'watchlist' instance, given the validated data
#         """
#         return WatchList.objects.create(**validated_data)
   
#     def update(self, instance, validated_data):
#         """
#         update and return an existing 'watchlist' instance, given the validated data
#         """
#         instance.title=validated_data.get('title', instance.title)
#         instance.storyLine=validated_data.get('storyLine', instance.storyLine)
#         instance.active=validated_data.get('active', instance.active)
#         instance.created=validated_data.get('created', instance.created)
#         instance.save()
#         return instance
    
# class StreamPlatformSerializer(serializers.Serializer):
#     id= serializers.IntegerField(read_only=True)
#     name=serializers.CharField(max_length=50)
#     about=serializers.CharField(max_length=50)
#     website=serializers.URLField(max_length=100)

#     def create(self, validated_data):
#         """
#         create instance of streamplatform 
#         """
#         return StreamPlatform.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         update and return an existing 'streamPlatform' instance, given the validated data
#         """
#         instance.name=validated_data.get('name', instance.name)
#         instance.about=validated_data.get('about', instance.about)
#         instance.website=validated_data.get('website', instance.website)
#         instance.save()
#         return instance
