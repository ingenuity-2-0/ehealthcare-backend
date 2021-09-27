from django.urls import path
from . import views

app_name = "heart_checkup"

urlpatterns = [
    path('', views.heart_checkup, name='heart_checkup'),
    path('checkup/', views.checkup, name='checkup')

]
