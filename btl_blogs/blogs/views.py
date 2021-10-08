from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


from .serializers import BlogSerializer
from .models import Blog

# Create your views here.


@api_view(['GET'])
def get_blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_blog(request, pk):
    blogs = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blogs, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes(['IsAuthenticated'])
def create_blog(request):
    data = request.data
    blog = Blog.objects.create(
        title=data['title'],
        content=data['content']
    )
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes(['IsAuthenticated'])
def update_blog(request, pk):
    data = request.data
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(instance=blog, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes(['IsAuthenticated'])
def delete_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return Response(f'The blog {Blog.title} has been successfully deleted')
