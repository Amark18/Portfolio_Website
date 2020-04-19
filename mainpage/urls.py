from django.urls import path
from .import views

from django.http import HttpResponse

urlpatterns = [
	path('', views.home),
	path('projects/<int:pk>/', views.project_detail, name='project_detail'),
]
