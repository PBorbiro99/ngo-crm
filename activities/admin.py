from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'location', 'project', 'organizer', 'max_participants']
    list_filter = ['event_date', 'project']
    search_fields = ['title', 'location']
    date_hierarchy = 'event_date'