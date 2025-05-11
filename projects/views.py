from django.shortcuts import render
from . models import Project

# Create your views here.

def projects(request):
    projectData = Project.objects.all().order_by("-project_updated_at")
    data = {
        "projectData": projectData,
    }
    return render(request, "projects.html", data)
