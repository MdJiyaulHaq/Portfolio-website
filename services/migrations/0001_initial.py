# Generated by Django 5.0.2 on 2024-12-18 07:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Services",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("service_icon", models.CharField(max_length=55)),
                ("service_title", models.CharField(max_length=55)),
                ("service_des", models.TextField()),
            ],
        ),
    ]
