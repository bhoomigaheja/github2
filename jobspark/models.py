# models.py
# models.py
from django.db import models

class ContactForm(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    company = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    message = models.TextField()

    def __str__(self):
        return self.name

ContactForm._meta.app_label = 'jobspark'


class UserData(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    # Add other fields as needed

    def __str__(self):
        return self.email




class Resume(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    position = models.CharField(max_length=100)
    about = models.TextField()

    # Fields for Experience
    experience_company1 = models.CharField(max_length=100, blank=True, null=True)
    experience_location1 = models.CharField(max_length=100, blank=True, null=True)
    experience_duration1 = models.CharField(max_length=20, blank=True, null=True)
    experience_role1 = models.CharField(max_length=100, blank=True, null=True)
    experience_description1 = models.TextField(blank=True, null=True)

   

    # Fields for Education
    education_institute1 = models.CharField(max_length=100, blank=True, null=True)
    education_location1 = models.CharField(max_length=100, blank=True, null=True)
    
    

    education_institute2 = models.CharField(max_length=100, blank=True, null=True)
    education_location2 = models.CharField(max_length=100, blank=True, null=True)
    
    education_institute3 = models.CharField(max_length=100, blank=True, null=True)
    education_location3= models.CharField(max_length=100, blank=True, null=True)
    
    
    # Fields for Projects
    project_name1 = models.CharField(max_length=100, blank=True, null=True)
    project_description1 = models.TextField(blank=True, null=True)

    project_name2 = models.CharField(max_length=100, blank=True, null=True)
    project_description2 = models.TextField(blank=True, null=True)

    # Fields for Skills
    skill1 = models.CharField(max_length=50, blank=True, null=True)
    skill2 = models.CharField(max_length=50, blank=True, null=True)
   
    # Fields for Interests
    interests = models.TextField(blank=True, null=True)
    
class Meta:
        ordering = ['-id']  # This ensures the latest record is retrieved based on the auto-incrementing 'id'
    
from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    repeat_password=models.CharField(max_length=255)


# In models.py
from django.db import models

class JobApplication(models.Model):
    job_title = models.CharField(max_length=255)
    cover_letter = models.TextField()

    def __str__(self):
        return self.job_title
