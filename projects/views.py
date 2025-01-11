from django.shortcuts import render
from django.views.generic import ListView
from  projects.models import post
# Create your views here.

class ListProjects(ListView):
    model=post 
    template_name="home.html"

