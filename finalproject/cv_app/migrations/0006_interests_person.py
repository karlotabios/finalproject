# Generated by Django 2.0.4 on 2018-04-29 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0005_auto_20180430_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='interests',
            name='person',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cv_app.Person'),
        ),
    ]
