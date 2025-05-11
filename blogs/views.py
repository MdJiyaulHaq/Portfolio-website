from django.shortcuts import render
from .models import Blog


# Create your views here.
def blogs(request):
    blogData = Blog.objects.all()
    data = {
        "blogData": blogData,
    }
    return render(request, "blogs.html", data)


def blogDetail(request, slug):
    blogData = Blog.objects.get(blog_slug=slug)
    data = {
        "blogData": blogData,
    }
    return render(request, "blogDetail.html", data)
