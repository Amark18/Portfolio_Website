# Generated by Django 3.0.5 on 2020-04-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(default='/image/background.png', path='webApp_Contact/My_Website/mainpage/static/images'),
        ),
    ]