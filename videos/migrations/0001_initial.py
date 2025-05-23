# Generated by Django 5.2 on 2025-05-07 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('class_name', models.CharField(blank=True, max_length=100)),
                ('entrance_exam', models.CharField(blank=True, max_length=100)),
                ('video', models.FileField(upload_to='video_lectures/')),
            ],
        ),
    ]
