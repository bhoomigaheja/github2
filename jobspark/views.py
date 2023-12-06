from django.http import HttpResponse
from django.shortcuts import render
from jobspark.scrapping1 import scrape_jobs
from jobspark.scrapping3 import gpt
from jobspark.scrapping2 import main
  # import your function from the Python file
# views.py in yourapp
from django.shortcuts import render, redirect
from .forms import ContactFormForm
from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from . base import authenticate_user



def index(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'blog.html')


def signn(request):
    return render(request,'sing-up.html')

def sign(request):
    return render(request,'sign-in.html')


def pricing(request):
    return render(request,'pricing.html')


def forgot(request):
    return render(request,'forgot.html')
def contact(request):
    return render(request,'contact.html')








from django.shortcuts import render
from django.http import HttpResponseBadRequest
 # Replace 'Job' with the actual model you are searching

def jobs_search(request):
    if request.method == 'POST':
        # Check if the user is logged in
        if request.user.is_authenticated:
            # Get the user's email
            user_email = request.user.email

            # Get the current count from the session or set it to 0
            search_count = request.session.get(f'search_count_{user_email}', 0)

            # Check if the user has exceeded the search limit
            if search_count >= 4:
                return HttpResponseBadRequest("Search limit exceeded.")

            # Increment the search count
            request.session[f'search_count_{user_email}'] = search_count + 1

        query = request.POST['query']
        data_dict_list = scrape_jobs(query)
        data_dict_list = data_dict_list[:24]

        # Print the data before rendering
        for job_data in data_dict_list:
            print(job_data)

        # Check if data_dict_list is not None before rendering
        if data_dict_list:
            return render(request, 'jobs.html', {'job_data_list': data_dict_list})
        else:
            # Handle the case where scrape_jobs returns an empty list
            return render(request, 'jobs.html', {'error_message': 'No data found'})
    else:
        return render(request, 'index.html')

# views.py

def submit_form(request):
    submitted = False

    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True  # Set the variable to indicate successful submission
    else:
        form = ContactFormForm()

    return render(request, 'contact.html', {'form': form, 'submitted': submitted})

# views.py
from django.shortcuts import render, redirect
from .models import UserData

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('Email-2')
        password = request.POST.get('Password-2')

        # Save user data to the database
        user_data = UserData.objects.create(email=email, password=password)

        # Redirect or render a response as needed
        return redirect('index.html')  # Replace 'success_page' with your actual success page URL

    return render(request, 'sign.html')  # Replace 'login.html' with your actual login page template
  # Replace with the actual module name where your scraping function is defined

def naukri_view2(request):
    if request.method == 'POST':
        query2 = request.POST.get('query2', '')
        job_data_list2 = main(query2)
        job_data_list2 = job_data_list2[:18]

        if job_data_list2:
            return render(request, 'naukri.html', {'query2': query2, 'job_data_list2': job_data_list2})
        else:
            return render(request, 'index.html', {'error_message': 'No data found'})

    return render(request, 'index.html')


def naukri_view(request):
    return render(request, 'naukri.html')
def times_view(request):
    return render(request, 'index.html')
# views.py


def show_resume_form(request):
    form = ResumeForm()
    return render(request, 'resumeform.html', {'form': form})

from django.shortcuts import render, redirect
from .models import Resume
from .forms import ResumeForm

# views.py
from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume

def submit_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            new_resume = form.save()
            return redirect('view_resume')
    else:
        form = ResumeForm()

    return render(request, 'resumeform.html', {'form': form})


def view_resume(request):
    try:
        # Retrieve the latest resume from the database based on the 'id' field
        latest_resume = Resume.objects.latest('id')
    except Resume.DoesNotExist:
        # Handle the case when no resumes are found
        latest_resume = None

    # Render the 'resume.html' template with the latest resume
    return render(request, 'resume.html', {'resume': latest_resume})

from .models import Resume

def show_resumes(request):
    resumes = Resume.objects.all()
    return render(request, 'show_resume_template.html', {'resumes': resumes})

from django.db import connection

from django.db import DatabaseError

from django.shortcuts import redirect

from django.shortcuts import render, redirect

def search_jobs(request):
    try:
        if request.method == 'POST':
            query = request.POST.get('query3', '')
            with connection.cursor() as cursor:
                sql_query = "SELECT * FROM job WHERE title LIKE %s"
                cursor.execute(sql_query, ['%' + query + '%'])
                results = cursor.fetchall()

                # Print the SQL query for debugging
                print(f"SQL Query: {cursor.mogrify(sql_query, ['%' + query + '%'])}")
                print(f"Query Results: {results}")

            return render(request, 'application.html', {'results': results})

        return render(request, 'index.html')

    except DatabaseError as e:
        print(f"Database Error: {e}")
        return render(request, 'index.html')

  # You can modify this based on your error handling strategy



def application_view(request):
    return render(request, 'application.html')
# views.py
# views.py
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form saved successfully")  # Check console for this message
            return render(request , 'sign-in.html')  # Adjust the URL pattern name accordingly
        else:
            print("Form is not valid:", form.errors)  # Check console for form validation errors
    else:
        form = SignUpForm()

    return render(request, 'sing-up.html', {'form': form})



def signup2(request):
    return render(request,'sing-up.html')

def sign(request):
    return render(request,'sign-in.html')    
# views.py


# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from .models import User

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            print("Email:", email)

            # Check if the user with the provided email exists
            try:
                user = User.objects.get(email=email)
                # If the user is found, redirect to index.html
                return redirect('index')
            except User.DoesNotExist:
                print('failed')
                messages.error(request, 'Invalid email. Please try again.')
                return render(request, 'sign-in.html', {'form': form})
            
        else:
            messages.error(request, 'Form is not valid. Please check your inputs.')
    else:
        form = LoginForm()

    return render(request, 'sign-in.html', {'form': form})

# views.py
from django.shortcuts import render
from jobspark.scrapping3 import gpt

from django.shortcuts import render

# views.py
from django.shortcuts import render
from .scrapping3 import gpt

def gpt_view(request):
    if request.method == 'POST':
        query = request.POST.get('query4')
        scraped_data = gpt(query)
        return render(request, 'gpt.html', {'scraped_data': scraped_data})

    return render(request, 'index.html') 


     # Render the form page for GET requests

  # Render the form page for GET requests

def gpt2(request):
    return render(request, 'gpt.html')
