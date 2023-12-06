# Generated by Django 4.2.6 on 2023-11-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(max_length=256)),
                ('country', models.CharField(max_length=256)),
                ('message', models.TextField()),
            ],
        ),
    ]
