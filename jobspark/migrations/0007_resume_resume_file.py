# Generated by Django 4.2.6 on 2023-11-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobspark', '0006_rename_education_degree1_resume_education_institute3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='resume_file',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
    ]