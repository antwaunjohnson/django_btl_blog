from rest_framework.generics import get_object_or_404
from blogs.models import Blog
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import BlogSerializer

# Blog Viewset


# class BlogViewSet(viewsets.ModelViewSet):

#     serializer_class = BlogSerializer
#     permission_classes = ([
#         permissions.IsAuthenticatedOrReadOnly
#     ])

#     def get_queryset(self):
#         return Blog.objects.all()

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Blog, id=item)

# class BlogViewSet(viewsets.ViewSet):
#     queryset = Blog.objects.all()
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly
#     ]

#     def list(self, request):
#         serializer_class = BlogSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         blog = get_object_or_404(self.queryset, pk=pk)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)
