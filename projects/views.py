from django.shortcuts import render, redirect
from django.views import generic
from .models import Project
class PostList(generic.ListView):
    queryset = Project.objects.filter(status=1).order_by('-created_on')
    template_name = 'projects/index.html'  # a list of all posts will be displayed on index.html

