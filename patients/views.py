from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    """Home page for Acuvere."""
    return render(request, 'patients/index.html')


@login_required
def health(request):
    """Page for users to view biometrics and health trends."""
    return render(request, 'patients/health.html')


@login_required
def appointments(request):
    """Page for users to view upcoming appointments."""
    return render(request, 'patients/appointments.html')


@login_required
def tasks(request):
    """Page for users to view tasks assigned by doctor."""
    return render(request, 'patients/tasks.html')
