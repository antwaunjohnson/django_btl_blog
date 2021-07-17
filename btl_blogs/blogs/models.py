from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    owner = models.ForeignKey(
        User, related_name="blogs", on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
