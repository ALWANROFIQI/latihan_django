# Generated by Django 5.1.2 on 2024-11-07 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('webpage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.webpage')),
            ],
        ),
    ]