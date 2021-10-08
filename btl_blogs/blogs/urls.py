from django.urls import path
from . import views


urlpatterns = [
    path('blogs/', views.get_blogs, name='blogs'),
    path('blogs/create', views.create_blog, name='create-blog'),
    path('blogs/<str:pk>/update', views.update_blog, name='update-blog'),
    path('blogs/<str:pk>/delete', views.delete_blog, name='delete-blog'),
    path('blogs/<str:pk>', views.get_blog, name='blog')
]
