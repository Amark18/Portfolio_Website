# Generated by Django 3.0.5 on 2020-04-16 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('short_description', models.TextField(default='')),
                ('long_description', models.TextField(default='')),
                ('technology', models.CharField(default='', max_length=200)),
                ('database', models.CharField(default='', max_length=200)),
                ('github_link', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
