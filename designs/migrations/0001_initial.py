# Generated by Django 5.0.6 on 2024-07-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('software', models.TextField(max_length=255)),
                ('description', models.TextField(default='The fruits of my hobbies', max_length=1000)),
            ],
        ),
    ]
