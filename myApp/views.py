
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class myView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset=Post.objects.all()
        