from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Patient(models.Model):
    """A patient and his/her appointments and tasks."""

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Patient.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Appointment(models.Model):
    """A patient's appointment and its associated info."""

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=500)


class Task(models.Model):
    """A task assigned to a patient by a healthcare worker."""

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    frequency = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
