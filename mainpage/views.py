from django.shortcuts import render
from django.http import HttpResponse
from mainpage.models import Project

def home(request):
	projects = Project.objects.all()
	context = {
        'projects': projects
    }
	return render(request, 'mainpage/homepage.html', context)

def project_detail(request, pk):
	project = Project.objects.get(pk=pk)
	context = {
		'project': project
	}
	return render(request, 'mainpage/project_detail.html', context)