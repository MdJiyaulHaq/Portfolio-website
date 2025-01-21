from django.shortcuts import render
from . models import Projects

# Create your views here.

def projects(request):
    projectData = Projects.objects.all().order_by("-project_added_at")
    data = {
        "projectData": projectData,
    }
    return render(request, "projects.html", data)
