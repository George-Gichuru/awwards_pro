from django.db import router
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from project.models import Post
from .serializers import  PostSerializer



@api_view(['GET'])
def get_links(request):
    endpoints = {
        'all':'/api/',
        
    }

    return Response(endpoints)

@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def single_post(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except:
        return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)