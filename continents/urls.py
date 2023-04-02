from django.urls import path
from . import views

urlpatterns = [
    path('', views.continents_all, name='continents'),
]