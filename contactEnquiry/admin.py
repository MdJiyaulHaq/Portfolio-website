from django.contrib import admin
from contactEnquiry.models import ContactEnquiry


# Register your models here.
class FormAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "password", "message")


admin.site.register(ContactEnquiry, FormAdmin)
