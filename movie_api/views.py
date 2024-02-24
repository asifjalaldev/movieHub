from django.shortcuts import render, HttpResponse
from .models import WatchList, StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer
# Create your views here.
def movie_list(request): 
    model_list=WatchList.objects.all()
    serialized=WatchListSerializer(model_list, many=True)

    print(serialized.data)
    return HttpResponse('testing movie list')
def movie_detail(request, pk):
    movie_detail=WatchList.objects.get(id=pk)
    serialized=WatchListSerializer(movie_detail)
    print(serialized.data)
    return HttpResponse(f'testing movie detail {pk}')