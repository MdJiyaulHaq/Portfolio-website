from django.contrib import admin
from blogs.models import blogDetail


# Register your models here.
class blogAdmin(admin.ModelAdmin):

    list_display = ("blog_title", "blog_des")


admin.site.register(blogDetail, blogAdmin)
