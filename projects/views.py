from django.shortcuts import render
from django.views.generic import ListView,DetailView 
from  projects.models import post

# Create your views here.

class ListProjects(ListView):
    model=post 
    template_name="home.html"

class DetailProjects(DetailView):
    model=post
    template_name="detail.html"