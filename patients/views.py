from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Patient, Appointment, Task
import json


def index(request):
    """Home page for Acuvere."""
    return render(request, 'patients/index.html')


@login_required
def health(request):
    """Page for users to view biometric summary, upcoming appointments, and tasks assigned."""
    appointments = Appointment.objects.filter(patient=request.user.patient)
    tasks = Task.objects.filter(patient=request.user.patient)
    biometric_data = json.load(open('patients/static/patients/biometric_data.json'))

    context = {
        'appointments': appointments,
        'tasks': tasks,
        'average_HR': sum(biometric_data['HourlyHeartRate']) / len(biometric_data['HourlyHeartRate']),
        'average_temp': sum(biometric_data['HourlyBodyTemp']) / len(biometric_data['HourlyBodyTemp']),
        'average_O2': sum(biometric_data['HourlySpO2']) / len(biometric_data['HourlySpO2']),
        'average_glucose': sum(biometric_data['HourlyBloodGlucose']) / len(biometric_data['HourlyBloodGlucose']),
        'user': request.user
    }
    return render(request, 'patients/health.html', context)


@login_required
def biometrics(request):
    """Page for users to view biometrics and health trends."""

    biometric_data = json.load(open('patients/static/patients/biometric_data.json'))

    context = {
        'biometrics': biometric_data
    }
    return render(request, 'patients/biometrics.html', context)


@login_required
def appointments(request):
    """Page for users to view upcoming appointments."""

    appointments = Appointment.objects.filter(patient=request.user.patient)

    context = {
        'appointments': appointments
    }
    return render(request, 'patients/appointments.html', context)


@login_required
def tasks(request):
    """Page for users to view tasks assigned by doctor."""

    tasks = Task.objects.filter(patient=request.user.patient)

    context = {
        'tasks': tasks
    }
    return render(request, 'patients/tasks.html', context)
