# Generated by Django 3.0.5 on 2020-04-16 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_auto_20200416_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.CharField(default='"background.png"', max_length=50),
        ),
    ]
