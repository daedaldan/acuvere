from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Patient, Appointment, Task
from plotly.offline import plot
import plotly.graph_objects as go
import datetime
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

    past_day = [datetime.time(hour=1),
                datetime.time(hour=2),
                datetime.time(hour=3),
                datetime.time(hour=4),
                datetime.time(hour=5),
                datetime.time(hour=6),
                datetime.time(hour=7),
                datetime.time(hour=8),
                datetime.time(hour=9),
                datetime.time(hour=10),
                datetime.time(hour=11),
                datetime.time(hour=12),
                datetime.time(hour=13),
                datetime.time(hour=14),
                datetime.time(hour=15),
                datetime.time(hour=16),
                datetime.time(hour=17),
                datetime.time(hour=18),
                datetime.time(hour=19),
                datetime.time(hour=20),
                datetime.time(hour=21),
                datetime.time(hour=22),
                datetime.time(hour=23),
                datetime.time(hour=0)]
    hr = biometric_data['HourlyHeartRate']
    temp = biometric_data['HourlyBodyTemp']
    oxygen = biometric_data['HourlySpO2']
    glucose = biometric_data['HourlyBloodGlucose']

    past_day_hr = go.Figure(go.Scatter(x=past_day, y=hr))
    past_day_hr.update_layout(
        title={
            'text': "Heart Rate Over Past 24 Hours",
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis_title="Hour",
        yaxis_title="Heart Rate",
        font=dict(
            family="Roboto",
            size=12,
            color="black"
        )
    )
    past_day_hr = past_day_hr.to_html(full_html=False, include_plotlyjs=False)

    past_day_temp = go.Figure(go.Scatter(x=past_day, y=temp))
    past_day_temp.update_layout(
        title={
            'text': "Body Temperature Over Past 24 Hours",
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis_title="Hour",
        yaxis_title="Body Temperature",
        font=dict(
            family="Roboto",
            size=12,
            color="black"
        )
    )
    past_day_temp = past_day_temp.to_html(full_html=False, include_plotlyjs=False)

    past_day_oxygen = go.Figure(go.Scatter(x=past_day, y=oxygen))
    past_day_oxygen.update_layout(
        title={
            'text': "Oxygen Saturation Over Past 24 Hours",
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis_title="Hour",
        yaxis_title="Oxygen Saturation",
        font=dict(
            family="Roboto",
            size=12,
            color="black"
        )
    )
    past_day_oxygen = past_day_oxygen.to_html(full_html=False, include_plotlyjs=False)

    past_day_glucose = go.Figure(go.Scatter(x=past_day, y=glucose))
    past_day_glucose.update_layout(
        title={
            'text': "Blood Glucose Over Past 24 Hours",
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis_title="Hour",
        yaxis_title="Blood Glucose",
        font=dict(
            family="Roboto",
            size=12,
            color="black"
        )
    )
    past_day_glucose = past_day_glucose.to_html(full_html=False, include_plotlyjs=False)

    context = {
        'biometrics': biometric_data,
        'past_day_hr': past_day_hr,
        'past_day_temp': past_day_temp,
        'past_day_oxygen': past_day_oxygen,
        'past_day_glucose': past_day_glucose,
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
