from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from blogs.models import Blogs
from projects.models import Projects
from contactEnquiry.models import ContactEnquiry


def home(request):
    projectData = Projects.objects.all().order_by("-project_added_at")[:2]
    blogData = Blogs.objects.all().order_by("-blog_added_at")[:3]
    data = {
        "projectData": projectData,
        "blogData": blogData,
    }
    return render(request, "index.html", data)


def blogDetail(request, slug):
    blogData = Blogs.objects.get(blog_slug=slug)
    data = {
        "blogData": blogData,
    }
    return render(request, "blogDetail.html", data)


def aboutMe(request):
    return render(request, "about.html")


def projects(request):
    projectData = Projects.objects.all()
    data = {
        "projectData": projectData,
    }
    return render(request, "projects.html", data)


def blogs(request):
    blogData = Blogs.objects.all()
    data = {
        "blogData": blogData,
    }
    return render(request, "blogs.html", data)


# views of main app


def contact(request):
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            message = request.POST.get("message")
        data = ContactEnquiry(
            name=name, email=email, password=password, message=message
        )
        data.save()
        return HttpResponseRedirect("/about/")
        return redirect("/about/", data)
    except:
        pass
    return render(request, "contact.html")
