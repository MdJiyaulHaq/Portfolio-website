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

