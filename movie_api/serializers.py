from rest_framework import serializers

from .models import WatchList, StreamPlatform

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
#  class base view---------------------------------

def checkLen(value):
    """
    this method is reusable validator. if we want a same validation logic for multiple models and fields
    then instead of specifying validate_filedName methods for each one, this approach is amazing.
    define single time and use multiple time 
    """
    if len(value) <3:
        raise serializers.ValidationError('filed value too short')
    return value

class WatchListSerializer(serializers.ModelSerializer):
    # if we need to validate multiple fields at once then we should use validate func which take data dictionary 
    # data {'fieldName' : 'value',. . .}
    title=serializers.CharField(validators=[checkLen])
    
    def validate(self, data):
        if data['title']== data['storyLine']:
            raise serializers.ValidationError('title should not be same as storyLine')
        return data
    class Meta:
        model=WatchList
        fields='__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):
       # to validate single field use validate_fieldName as func
    # def validate_name(self, value):
    #     if len(value)< 3:
    #         raise serializers.ValidationError('name is too short')
    #     return value
    """using reusable validator func instead of above field_validate method"""
    name=serializers.CharField(validators=[checkLen])
    class Meta:
        model=StreamPlatform
        fields='__all__'
    
    