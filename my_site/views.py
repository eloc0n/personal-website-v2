from django.shortcuts import render

from .models import Project, Social, Video
# Create your views here.
def index(request):

    projects = Project.objects.all()
    socials = Social.objects.all()
    videos = Video.objects.all()

    context = {
        "projects":projects,
        "socials":socials,
        "videos":videos,
    }   

    return render(request, 'index.html', context)


