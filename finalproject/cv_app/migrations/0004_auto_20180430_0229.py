# Generated by Django 2.0.4 on 2018-04-29 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0003_education_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='period',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='period',
            field=models.DateField(),
        ),
    ]
