from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    data = {
        "title": "Home Page",
        "plist": ["Java", "Python", "Django"],
        "students": [
            {"name": "Brajesh", "phone": 9834543345},
            {"name": "Bikram", "phone": 9857543345},
            {"name": "Shankar", "phone": 9865543345},
            {"name": "Hari", "phone": 9807543345},
        ],
        "numbers": [1, 2, 3, 4, 5, 6],
    }
    return render(request, "index.html", data)


def aboutUs(request):
    return HttpResponse("Welcome to my website.")


def course(request):
    return HttpResponse("these are the courses")


def courseDetails(request, courseId):
    return HttpResponse(courseId)
