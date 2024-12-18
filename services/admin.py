from django.contrib import admin
from services.models import Services


# Register your models here.
class serviceAdmin(admin.ModelAdmin):
    # When you display a Model as a list,
    # Django displays each record as the string representation of the record object
    list_display = ("service_icon", "service_title", "service_des")


admin.site.register(Services, serviceAdmin)
