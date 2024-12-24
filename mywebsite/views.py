from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from blogs.models import Blogs
from services.models import Services


def home(request):
    blogData = Blogs.objects.all()[:2]
    data = {
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
    return render(request, "projects.html")


def blogs(request):
    blogData = Blogs.objects.all()
    data = {
        "blogData": blogData,
    }
    return render(request, "blogs.html", data)


# views of main app
def services(request):
    # to limit the query results
    # cannot use negative indexing
    servicesData = Services.objects.all().order_by("-service_title")
    if request.method == "GET":
        searchData = request.GET.get("serviceName")
        if searchData != None:
            servicesData = Services.objects.filter(service_title__icontains=searchData)
    data = {"servicesData": servicesData}
    return render(request, "services.html", data)


def form(request):
    try:
        if request.method == "POST":
            n1 = request.POST.get("name")
            n2 = request.POST.get("email")
            n3 = request.POST.get("message")
            n4 = request.POST.get("password")
        data = {
            "n1": n1,
            "n2": n2,
            "n3": n3,
            "n4": n4,
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
