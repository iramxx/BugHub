from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Bug

class SignupForm(UserCreationForm):
    ROLE_choices = [
        ('researcher', 'Security Researcher'),
        ('company', 'Company'),
    ]

    class Meta:
        model = User
        fields = ["username", "email", "role", "password1", "password2"]   

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ["title", "company", "description", "level", "evidence"]
