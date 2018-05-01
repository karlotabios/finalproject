# Generated by Django 2.0.4 on 2018-04-29 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('school', models.CharField(max_length=100)),
                ('period', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('interests', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('school', models.CharField(max_length=100)),
                ('period', models.DateTimeField()),
                ('description', models.TextField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv_app.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='education',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv_app.Person'),
        ),
    ]
