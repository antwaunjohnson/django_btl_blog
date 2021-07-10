from blogs.models import Blog
from rest_framework import viewsets, permissions
from .serializers import BlogSerializer

# Blog Viewset


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = BlogSerializer
