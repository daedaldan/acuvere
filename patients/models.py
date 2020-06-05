from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


class Patient(models.Model):
    """A patient and his/her appointments and tasks."""

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    user = models.OneToOneField(User, related_name="patient", blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    @receiver(post_save, sender=User)
    def create_save_user_profile(sender, instance, created, **kwargs):
        if created:
            Patient.objects.create(user=instance)
        instance.patient.save()


class Appointment(models.Model):
    """A patient's appointment and its associated info."""

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    location = models.CharField(max_length=25)
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=500)


class Task(models.Model):
    """A task assigned to a patient by a healthcare worker."""

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    frequency = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
