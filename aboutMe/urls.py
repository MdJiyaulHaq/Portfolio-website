from django.urls import path
from .views import aboutMe

urlpatterns = [
    path("", aboutMe, name="about"),
]
