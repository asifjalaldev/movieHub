from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import WatchList, StreamPlatform, Review
from rest_framework.views import APIView
from django.http import Http404
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework import mixins, generics
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.serializers import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import permission_classes
from .permissions import CustomReviewUserOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import UserRateThrottle
# Create your views here.
# creating entry point of our api-----------
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def api_root(request):
    return Response({
        # 'streamList': reverse('streamplatform', request=request),
        # 'watchList': reverse('movie-list', request=request)
    })

# using veiwsets for crud oprations------------
class streamPlatformVeiwsets(viewsets.ModelViewSet):

    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    throttle_classes=[UserRateThrottle]
    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
class WatchListViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    authentication_classes=[JWTAuthentication]
    queryset=WatchList.objects.all()
    serializer_class=WatchListSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
class ReviewListView(generics.ListAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(watchList=pk)
class ReviewCreateView(generics.CreateAPIView):
    # permission_classes=[CustomAdminOrReadOnly]
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user) # explicitly set user from request
        pk=self.kwargs['pk']
        movie=WatchList.objects.get(id=pk)
        reviewed=Review.objects.filter(user=self.request.user, watchList=movie).first()
        if reviewed:
            print(f'--------------{movie.title} already reviewed by {self.request.user.username}')
            raise ValidationError(f'{movie.title} already reviewed by {self.request.user.username}')
        else:
            serializer.save(watchList=movie)
        if movie.number_rating == 0:
            movie.avg_rating=serializer.validated_data['rating']
        else:
            movie.avg_rating=(movie.avg_rating + serializer.validated_data['rating'])/2
        movie.number_rating+=1
        movie.save()
        print('movie no of rating', movie.number_rating)
        print('movie avg rating', movie.avg_rating)
        serializer.save(WatchList=movie, user=self.request.user)
        # return super().perform_create(serializer)
    
    
class ReviewListDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[CustomReviewUserOrReadOnly]
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

# using already mixed generics classes-----------
# class Stream(generics.ListCreateAPIView):
#     queryset=StreamPlatform.objects.all()
#     serializer_class=StreamPlatformSerializer

# class StreamDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=StreamPlatform.objects.all()
#     serializer_class=StreamPlatformSerializer

# class watchListView(generics.ListCreateAPIView):
#     queryset=WatchList.objects.all()
#     serializer_class=WatchListSerializer

# class watchListDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=WatchList.objects.all()
#     serializer_class=WatchListSerializer
    
# mixins uses for crud---------------------
# class Stream(mixins.ListModelMixin, mixins.CreateModelMixin
#                  ,generics.GenericAPIView):
#     queryset = StreamPlatform.objects.all()
#     serializer_class= StreamPlatformSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class StreamDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    generics.GenericAPIView):
#     queryset=StreamPlatform.objects.all()
#     serializer_class=StreamPlatformSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
# class watchListView(mixins.ListModelMixin, mixins.CreateModelMixin,
#                     generics.GenericAPIView):
#     queryset=WatchList.objects.all()
#     serializer_class=WatchListSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class watchListDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin,
#                           generics.GenericAPIView):
#     queryset=WatchList.objects.all()
#     serializer_class=WatchListSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
# class base views------------------------
# class Stream(APIView):
#     def get(self, request):
#         model_list=StreamPlatform.objects.all()
#         serialized=StreamPlatformSerializer(model_list, many=True)
#         return Response(serialized.data)
#     def post(self, request):
#         serialized=StreamPlatformSerializer(data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

# class StreamDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return StreamPlatform.objects.get(id=pk)
#         except StreamPlatform.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk):
#         stream=self.get_object(pk)
#         serializer=StreamPlatformSerializer(stream)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         stream=self.get_object(pk)
#         serializer=StreamPlatformSerializer(stream, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         stream=self.get_object(pk)
#         stream.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class watchListView(APIView):
#     def get(self, request):
#         watch=WatchList.objects.all()
#         serializer=WatchListSerializer(watch, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         watch_obj=WatchListSerializer(data=request.data)
#         if watch_obj.is_valid():
#             watch_obj.save()
#             return Response(watch_obj.data)
#         return Response(watch_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class watchListDetailView(APIView):
#     def get_obj(self, pk):
#         try:
#             watchObj=WatchList.objects.get(id=pk)
#             return watchObj
#         except WatchList.DoesNotExist:
#             raise Http404
#     def get(self, request, pk):
#         obj=self.get_obj(pk)
#         serialize=WatchListSerializer(obj)
#         return Response(serialize.data)
    
#     def put(self, request, pk):
#         watchObj=self.get_obj(pk)
#         serialize=WatchListSerializer(watchObj, data=request.data)
#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data)
#         return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk):
#         watchObj=self.get_obj(pk)
#         watchObj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    


# functional base views----------------
# @api_view(['GET', 'POST'])
# def movie_list(request): 
#     if request.method=='GET':
#         model_list=WatchList.objects.all()
#         serialized=WatchListSerializer(model_list, many=True)
#         return Response(serialized.data)
#     elif request.method=='POST':
#         serialized=WatchListSerializer(data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET', 'POST'])
# def movie_detail(request, pk):
#     if request.method=='GET':
#         movie_detail=WatchList.objects.get(id=pk)
#         serialized=WatchListSerializer(movie_detail)
#         return Response(serialized.data)
    
# @api_view(['GET', 'POST'])
# def stream_list(request): 
#     if request.method=='GET':
#         model_list=StreamPlatform.objects.all()
#         serialized=StreamPlatformSerializer(model_list, many=True)
#         return Response(serialized.data)
#     elif request.method=='POST':
        
#         serialized=StreamPlatformSerializer(data = request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
 
#     return Response(serialized)
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def stream_detail(request, pk):
#     try:
#         stream=StreamPlatform.objects.get(id=pk)
#     except stream.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method== 'GET':
#         serialized=StreamPlatformSerializer(stream)
#         return Response(serialized.data)
#     elif request.method == 'PUT':
#         print('inside put', stream)
#         serialized=StreamPlatformSerializer(stream, data = request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method=='DELETE':
#         stream.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    