from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField


# Create your models here.
class Project(models.Model):
    project_added_at = models.DateTimeField(auto_now_add=True)
    project_updated_at = models.DateTimeField(auto_now=True)
    project_title = models.CharField(max_length=255)
    project_des = HTMLField()
    project_technology = models.CharField(max_length=255)
    project_link= models.URLField()
    live_link = models.URLField()
    project_slug = AutoSlugField(
        populate_from="project_title", unique=True, null=True, default=None
    )
