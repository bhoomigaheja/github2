from django import forms
from .models import ContactForm
from .models import Resume    # Ensure this import is correct

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'
class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
# forms.py
from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

from django import forms

class LoginForm(forms.Form):
  email = forms.EmailField()

        
