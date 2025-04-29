from django.contrib import admin
from projects.models import Projects


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "project_added_at",
        "project_updated_at",
        "project_title",
        "project_technology",
        "project_des",
        "project_slug",
        "project_link",
    )


admin.site.register(Projects, ProjectAdmin)
