from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class blogDetail(models.Model):
    blog_title = models.CharField(max_length=255)
    blog_des = HTMLField()