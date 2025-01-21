from django.shortcuts import render
from .models import Blogs


# Create your views here.
def blogs(request):
    blogData = Blogs.objects.all()
    data = {
        "blogData": blogData,
    }
    return render(request, "blogs.html", data)


def blogDetail(request, slug):
    blogData = Blogs.objects.get(blog_slug=slug)
    data = {
        "blogData": blogData,
    }
    return render(request, "blogDetail.html", data)
