from django.http import HttpResponseRedirect
from django.shortcuts import render

from contactEnquiry.models import ContactEnquiry


# Create your views here.
def contact(request):
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")
        data = ContactEnquiry(name=name, email=email, message=message)
        data.save()
        return HttpResponseRedirect("/about/", data)
    except Exception as e:
        print(e)
    return render(request, "contact.html")
