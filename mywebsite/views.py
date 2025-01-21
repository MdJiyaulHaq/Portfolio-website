from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from blogs.models import Blogs
from projects.models import Projects
from contactEnquiry.models import ContactEnquiry


def home(request):
    projectData = Projects.objects.all().order_by("-project_added_at")[:4]
    blogData = Blogs.objects.all().order_by("-blog_added_at")[:3]
    data = {
        "projectData": projectData,
        "blogData": blogData,
    }
    return render(request, "index.html", data)


def aboutMe(request):
    return render(request, "about.html")


def projects(request):
    projectData = Projects.objects.all().order_by("-project_added_at")
    data = {
        "projectData": projectData,
    }
    return render(request, "projects.html", data)


def contact(request):
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")
        data = ContactEnquiry(name=name, email=email, message=message)
        data.save()
        return HttpResponseRedirect("/about/", data)
    except Exception as e:
        print(e)
    return render(request, "contact.html")
