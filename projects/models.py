from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField


# Create your models here.
class Projects(models.Model):
    project_title = models.CharField(max_length=255)
    project_des = HTMLField()
    project_technology = models.CharField(max_length=512)
    project_link= models.URLField()
    project_slug = AutoSlugField(
        populate_from="project_title", unique=True, null=True, default=None
    )
