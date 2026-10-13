from django.contrib import admin
from .models import Project, Task, Comment

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ["project"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_at"]










admin.site.register(Comment)
# Register your models here.
