from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def aboutUs(request):
    return HttpResponse("Welcome to my website.")


def course(request):
    return HttpResponse("these are the courses")


def courseDetails(request, courseId):
    return HttpResponse(courseId)
