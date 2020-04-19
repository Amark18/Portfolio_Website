from django.db import models

# Create your models here.

class Project(models.Model):
	title 		= models.CharField(default='', max_length=200)
	short_description = models.TextField(default='')
	long_description = models.TextField(default='')
	technology 	= models.CharField(default='', max_length=200)
	database 	= models.CharField(default='', max_length=200)
	github_link = models.CharField(default='', max_length=50)
	image = models.CharField(default='images/background.png', max_length=50)

	class Meta:
		app_label = 'mainpage'

	def __str__(self):
		return self.title