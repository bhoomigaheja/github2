# Generated by Django 4.2.6 on 2023-11-17 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobspark', '0005_resume_delete_userdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='education_degree1',
            new_name='education_institute3',
        ),
        migrations.RenameField(
            model_name='resume',
            old_name='education_degree2',
            new_name='education_location3',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='education_description1',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='education_description2',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='education_duration1',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='education_duration2',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='experience_company2',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='experience_description2',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='experience_duration2',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='experience_location2',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='experience_role2',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='skill3',
        ),
    ]
