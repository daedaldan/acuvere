from django.urls import path

from . import views

app_name = 'patients'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('health/', views.health, name='health'),
    path('appointments/', views.appointments, name='appointments'),
    path('tasks/', views.tasks, name='tasks'),
]
