from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class StreamPlatform(models.Model):

    name=models.CharField(max_length=50)
    about=models.CharField(max_length=50)
    website=models.URLField(max_length=100)
    def __str__(self):
        return self.name

class WatchList(models.Model):

    title=models.CharField(max_length=50)
    storyLine=models.CharField(max_length=100)
    platform=models.ForeignKey(StreamPlatform, on_delete=models.CASCADE)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    avg_rating=models.FloatField(default=0.0)
    number_rating=models.IntegerField(default=0)
    # when only update need use auto_now and when created use auto_now_add
    def __str__(self):
        return self.title
    
class Review(models.Model):

    rating=models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    desc=models.CharField(max_length=100)
    watchList= models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='related_watchlist')
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='related_user', default=1)
    active=models.BooleanField(default=True)
    created= models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        string=str(self.rating) + " "+ self.watchList.title
        return string
    