# Generated by Django 5.0.2 on 2024-12-30 07:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("contactEnquiry", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contactenquiry",
            name="password",
        ),
    ]
