from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm

def register(request):
    """Register a new patient."""

    form = RegistrationForm(request.POST)

    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.patient.first_name = form.cleaned_data.get('first_name')
        user.patient.last_name = form.cleaned_data.get('last_name')
        user.patient.email = form.cleaned_data.get('email')
        user.patient.birth_date = form.cleaned_data.get('birth_date')
        user.patient.gender = form.cleaned_data.get('gender')
        user.save()

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        # Log in, redirect to home page
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('patients:index')
    else:
        form = RegistrationForm()

    # Display blank or invalid form.
    context = {
        'form': form
        }
    return render(request, 'registration/register.html', context)
