# Generated by Django 3.2.20 on 2023-09-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_task', '0002_task_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestingTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
