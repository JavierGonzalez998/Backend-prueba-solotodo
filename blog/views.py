from .models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from datetime import datetime
from django.shortcuts import get_object_or_404


class PostViewSet(APIView):
    def get(self, req):
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, req):
        title = req.data["title"]
        content = req.data["content"]
        author = req.data["author"]
        obj = Post.objects.create(title = title, content=content, author = author,created_at = datetime.now())
        if(obj):
            serializer = PostSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Error al publicar el post, ingrese nuevamente"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PostDetail(APIView):
    def get(self, req, id):
        id = get_object_or_404(Post, pk=id)
        serializer = PostSerializer(id)
        return Response(serializer.data, status=status.HTTP_200_OK)