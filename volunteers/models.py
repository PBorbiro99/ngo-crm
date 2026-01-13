from django.db import models
from users.models import User
from projects.models import Project

class VolunteerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='volunteer_profile')
    skills = models.TextField(blank=True)
    availability = models.CharField(max_length=100, blank=True)
    emergency_contact = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"Volunteer: {self.user.username}"

class VolunteerActivity(models.Model):
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='volunteer_activities')
    activity_date = models.DateField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.volunteer.username} - {self.project.title} ({self.hours_worked}h)"