# Generated by Django 5.0.1 on 2024-02-06 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_censorinfo_movieinfo_censor_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='directed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='directed_movies', to='movies.director'),
        ),
    ]