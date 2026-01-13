from django.db import models
from projects.models import Project
from users.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name='events')
    organizer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    max_participants = models.IntegerField(default=50)
    
    def __str__(self):
        return self.title