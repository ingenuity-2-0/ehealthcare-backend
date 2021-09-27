from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('covid19/', views.covid19, name='covid19')
]
