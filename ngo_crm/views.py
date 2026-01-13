from django.shortcuts import render, get_object_or_404, redirect
from donors.models import Donor, Donation
from projects.models import Project

def home(request):
    return render(request, 'home.html')

def donor_list(request):
    donors = Donor.objects.all()
    return render(request, 'donors/donor_list.html', {'donors': donors})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})