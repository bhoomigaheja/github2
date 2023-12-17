# Generated by Django 4.2.6 on 2023-11-16 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobspark', '0004_userdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('position', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('experience_company1', models.CharField(blank=True, max_length=100, null=True)),
                ('experience_location1', models.CharField(blank=True, max_length=100, null=True)),
                ('experience_duration1', models.CharField(blank=True, max_length=20, null=True)),
                ('experience_role1', models.CharField(blank=True, max_length=100, null=True)),
                ('experience_description1', models.TextField(blank=True, null=True)),
                ('experience_company2', models.CharField(blank=True, max_length=100, null=True)),
                ('experience_location2', models.CharField(blank=True, max_length=100, null=True)),
                ('experience_duration2', models.CharField(blank=True, max_length=20, null=True)),
                ('experience_role2', models.CharField(blank=True, max_length=100, null=True)),
                ('experience_description2', models.TextField(blank=True, null=True)),
                ('education_institute1', models.CharField(blank=True, max_length=100, null=True)),
                ('education_location1', models.CharField(blank=True, max_length=100, null=True)),
                ('education_duration1', models.CharField(blank=True, max_length=20, null=True)),
                ('education_degree1', models.CharField(blank=True, max_length=100, null=True)),
                ('education_description1', models.TextField(blank=True, null=True)),
                ('education_institute2', models.CharField(blank=True, max_length=100, null=True)),
                ('education_location2', models.CharField(blank=True, max_length=100, null=True)),
                ('education_duration2', models.CharField(blank=True, max_length=20, null=True)),
                ('education_degree2', models.CharField(blank=True, max_length=100, null=True)),
                ('education_description2', models.TextField(blank=True, null=True)),
                ('project_name1', models.CharField(blank=True, max_length=100, null=True)),
                ('project_description1', models.TextField(blank=True, null=True)),
                ('project_name2', models.CharField(blank=True, max_length=100, null=True)),
                ('project_description2', models.TextField(blank=True, null=True)),
                ('skill1', models.CharField(blank=True, max_length=50, null=True)),
                ('skill2', models.CharField(blank=True, max_length=50, null=True)),
                ('skill3', models.CharField(blank=True, max_length=50, null=True)),
                ('interests', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UserDetail',
        ),
    ]