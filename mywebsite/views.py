from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("Welcome to my website.")

def course(request):
    return HttpResponse("these are the courses")

def courseDetails(request,courseId):
    return HttpResponse(courseId)