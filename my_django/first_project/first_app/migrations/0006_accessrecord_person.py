# Generated by Django 5.1.2 on 2024-11-08 12:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_person_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessrecord',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='first_app.person'),
        ),
    ]
