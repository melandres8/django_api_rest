from django.http import JsonResponse

# Restful Api dependencies
from rest_framework.views import APIView
from rest_framework.response import Response
# Serializer
from .models import Post
from .serializers import PostSerializer


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        query_set = Post.objects.all()
        serializer = PostSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
