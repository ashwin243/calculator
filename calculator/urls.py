from django.urls import path
from . import views

urlpatterns = [
    path('', views.age_calculator_view, name='home'),
]
