from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import PatientForm

def register(request):
    """Register a new patient."""

    if request.method != 'POST':
        # Display blank registration form.
        user_form = UserCreationForm()
        patient_form = PatientForm()

    else:
        # Process completed form.
        user_form = UserCreationForm(data=request.POST)
        patient_form = PatientForm(data=request.POST)

        if user_form.is_valid() and patient_form.is_valid():
            new_user = user_form.save()

            # Log in, redirect to home page
            login(request, new_user)
            return redirect('patients:index')

    # Display blank or invalid form.
    context = {
        'user_form': user_form,
        'patient_form': patient_form
        }
    return render(request, 'registration/register.html', context)
