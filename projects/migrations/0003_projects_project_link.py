# Generated by Django 5.0.2 on 2024-12-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_projects_project_technology"),
    ]

    operations = [
        migrations.AddField(
            model_name="projects",
            name="project_link",
            field=models.URLField(default="exit"),
            preserve_default=False,
        ),
    ]
