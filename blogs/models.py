from autoslug import AutoSlugField
from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Blogs(models.Model):
    blog_date = models.DateTimeField(auto_now_add=True)
    blog_title = models.CharField(max_length=255)
    blog_overview = models.CharField(max_length=255)
    blog_des = HTMLField()
    blog_slug = AutoSlugField(
        populate_from="blog_title", unique=True, null=True, default=None
    )
