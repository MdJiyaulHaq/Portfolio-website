# Generated by Django 5.0.2 on 2024-12-28 05:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0004_blogs_blog_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogs",
            name="blog_overview",
            field=models.CharField(default="exit", max_length=255),
            preserve_default=False,
        ),
    ]