from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'

    absolute_url = serializers.URLField(
        source='get_absolute_url', read_only=True)
