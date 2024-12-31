from django.contrib import admin
from blogs.models import Blogs


# Register your models here.
class blogAdmin(admin.ModelAdmin):

    list_display = ("blog_added_at","blog_title", "blog_des", "blog_slug", "blog_overview")


admin.site.register(Blogs, blogAdmin)