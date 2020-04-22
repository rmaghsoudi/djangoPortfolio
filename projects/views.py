from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def homepage(req):
  projects = Project.objects
  return render(req, 'projects/home.html', {'projects': projects})

def detail(req, project_id):
  project_detail = get_object_or_404(Project, pk=project_id)
  return render(req, 'projects/detail.html', {'project': project_detail})