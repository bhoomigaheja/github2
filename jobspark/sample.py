# insert_sample_data.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobspark.settings')
django.setup()

from models import JobApplication

# Sample data
data = [
    ("student", "i love you"),
    ("python developer", "INSERT INTO job_applications (cover_letter) VALUES ..."),
    ("python developer", "I hope this message finds you well. ..."),
    ("php developer", "I hope this message finds you well. ..."),
    ("software developer", "I hope this message finds you well. ..."),
]

# Populate the JobApplication table
for job_title, cover_letter in data:
    JobApplication.objects.create(job_title=job_title, cover_letter=cover_letter)

print("Sample data inserted successfully.")
