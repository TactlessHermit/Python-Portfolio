# Generated by Django 5.0.6 on 2024-07-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=250)),
                ('genre', models.TextField(max_length=250)),
                ('video_link', models.URLField(max_length=2000)),
            ],
        ),
    ]
