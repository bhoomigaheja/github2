# Generated by Django 4.2.6 on 2023-11-12 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobspark', '0002_rename_contactformsubmission_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
