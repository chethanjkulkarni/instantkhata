# Generated by Django 3.0.6 on 2020-07-05 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesman', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='salesman',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]