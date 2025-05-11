from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from blogs.models import Blog
from projects.models import Project
from contactEnquiry.models import ContactEnquiry


def home(request):
    projectData = Project.objects.all().order_by("-project_updated_at")[:4]
    blogData = Blog.objects.all().order_by("-blog_added_at")[:3]
    data = {
        "projectData": projectData,
        "blogData": blogData,
    }
    return render(request, "index.html", data)
