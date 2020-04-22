from django.shortcuts import render
from .models import Project

# Create your views here.
def homepage(req):
  projects = Project.objects
  return render(req, 'projects/home.html', {'projects': projects})