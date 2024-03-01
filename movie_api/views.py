from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import WatchList, StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer
# Create your views here.
@api_view(['GET', 'POST'])
def movie_list(request): 
    if request.method=='GET':
        model_list=WatchList.objects.all()
        serialized=WatchListSerializer(model_list, many=True)
        return Response(serialized.data)
    elif request.method=='POST':
        serialized=WatchListSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'POST'])
def movie_detail(request, pk):
    if request.method=='GET':
        movie_detail=WatchList.objects.get(id=pk)
        serialized=WatchListSerializer(movie_detail)
        return Response(serialized.data)
    
@api_view(['GET', 'POST'])
def stream_list(request): 
    if request.method=='GET':
        model_list=StreamPlatform.objects.all()
        serialized=StreamPlatformSerializer(model_list, many=True)
        return Response(serialized.data)
    elif request.method=='POST':
        
        serialized=StreamPlatformSerializer(data = request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
 
    return Response(serialized)
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def stream_detail(request, pk):
    try:
        stream=StreamPlatform.objects.get(id=pk)
    except stream.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method== 'GET':
        serialized=StreamPlatformSerializer(stream)
        return Response(serialized.data)
    elif request.method == 'PUT':
        print('inside put', stream)
        serialized=StreamPlatformSerializer(stream, data = request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        stream.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    