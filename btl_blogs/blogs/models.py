
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.contrib.auth.models import User

from .utils import slugify_instance_title

STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Blog(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=True, blank=True, unique=True)
    content = models.TextField()
    created_by = models.ForeignKey(
        User, related_name="blogs", on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def get_absolute_url(self):
        return reverse("blog", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        # if self.slug is None:
        #     slugify_instance_title(self, save=False)
        super().save(*args, **kwargs)


def blog_pre_save(sender, instance, *args, **kwargs):
    # print('pre_save')
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(blog_pre_save, sender=Blog)


def blog_post_save(sender, instance, created, *args, **kwargs):
    # print('post_save')
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(blog_post_save, sender=Blog)
