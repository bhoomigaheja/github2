"""
URL configuration for jobspark project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from .views import submit_form
from .views import naukri_view2
from .views import naukri_view
from .views import times_view
from .views import submit_resume
from. views import signup
from. views import login_user


from .views import search_jobs
from . views import gpt_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name = 'index'),
    path('blog/', views.blog, name = 'blog'),
    path('sign-in/', views.sign, name = 'sign'),
    path('sing-up/', views.signn, name = 'signn'),
    path('pricing/', views.pricing, name = 'pricing'),
      
    path('forgot/', views.forgot, name = 'forgot'),
    path('contact/', views.contact, name = 'contact'),
    path('jobs/', views.jobs_search, name='jobs_search'),
    path('jobs2/', views.naukri_view2, name='naukri_view2'),
    path('job-location/miami-fl',views.naukri_view, name='naukri_view'),
    path('submit_form/', views.submit_form, name='submit_form'),
    path('job-location/jobspark/templates/index.html',views.times_view, name='times_view'),
    path('show_resume_form/', views.show_resume_form, name='show_resume_form'),
    path('view_resume/', views.view_resume, name='view_resume'),
    path('show_resumes/', views.show_resumes, name='show_resumes'),
    path('submit_resume/', views.submit_resume, name='submit_resume'),
    path('search_jobs/', views.search_jobs, name='search_jobs'),

    path('application_view/', views.application_view, name='application_view'),
    path('submit_resume/', views.submit_resume, name='submit_resume'),
    path('signup2/', views.signup2, name='signup2'),
    path('', views.signup, name='signup'),
    path('sign/', views.sign, name='sign'),
    path('login/', views.login_user, name='login_user'),
    
    path('gpt2/', views.gpt2, name='gpt2'),
    path('gpt/', gpt_view, name='gpt_view'),
]


    


 
      

