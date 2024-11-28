from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    data = {"title": "Home Page"}
    return render(request, "index.html", data)


def aboutUs(request):
    return HttpResponse("Welcome to my website.")


def course(request):
    return HttpResponse("these are the courses")


def courseDetails(request, courseId):
    return HttpResponse(courseId)
