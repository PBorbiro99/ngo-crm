from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'start_date', 'end_date', 'budget', 'manager']
    list_filter = ['status', 'start_date']
    search_fields = ['title', 'description']
    date_hierarchy = 'start_date'