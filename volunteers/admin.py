from django.contrib import admin
from .models import VolunteerProfile, VolunteerActivity

@admin.register(VolunteerProfile)
class VolunteerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'skills', 'availability']
    search_fields = ['user__username', 'skills']

@admin.register(VolunteerActivity)
class VolunteerActivityAdmin(admin.ModelAdmin):
    list_display = ['volunteer', 'project', 'activity_date', 'hours_worked']
    list_filter = ['activity_date', 'project']
    search_fields = ['volunteer__username', 'project__title']