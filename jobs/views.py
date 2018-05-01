from django.shortcuts import render

from .models import Job

def home(request):
    #get jobs from database
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})
