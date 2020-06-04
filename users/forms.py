from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from patients.models import Patient


class RegistrationForm(UserCreationForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)
    birth_date = forms.DateField()
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER_CHOICES))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password1', 'password2', 'birth_date', 'gender')
