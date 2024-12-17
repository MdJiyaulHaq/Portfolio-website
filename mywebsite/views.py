from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


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


def aboutMe(request):
    return render(request, "about.html")


def projects(request):
    return render(request, "projects.html")

def blogs(request):
    return render(request, "blogs.html")

def form(request):
    try:
        if request.method == "POST":
            n1= request.POST.get("name")
            n2= request.POST.get('email')
            n3= request.POST.get('message')
            n4= request.POST.get('password')
        data={
            "n1":n1,
            "n2":n2,
            "n3":n3,
            "n4":n4,
        }
        return HttpResponseRedirect("/about/", data)
        return redirect("/about/", data)
    except:
        pass
    return render(request, "form.html")

def course(request):
    return HttpResponse("these are the courses")


def courseDetails(request, courseId):
    return HttpResponse(courseId)
