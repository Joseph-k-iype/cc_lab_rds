from django.urls import path

from . import views

urlpatterns = [
    path('', views.covid, name='covid'),
    path('covid_dash/', views.covid_dash, name='covid_dash'),
]