from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from blogs.models import Blogs
from services.models import Services
from contactEnquiry.models import ContactEnquiry


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
    return render(request, "form.html")


def course(request):
    return HttpResponse("these are the courses")


def courseDetails(request, courseId):
    return HttpResponse(courseId)
