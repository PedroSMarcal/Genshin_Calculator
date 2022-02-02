from django.urls import path
from . import views

urlpatterns = [
    path('farms/', views.get, name='teste')
]