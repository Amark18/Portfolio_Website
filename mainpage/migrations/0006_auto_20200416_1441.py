# Generated by Django 3.0.5 on 2020-04-16 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_auto_20200416_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.CharField(default='images/background.png', max_length=50),
        ),
    ]