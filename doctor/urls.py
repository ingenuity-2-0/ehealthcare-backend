from django.urls import path
from . import views

app_name = "doctor"

urlpatterns = [
    path('name_search/', views.name_search, name='name_search'),
    path('symptoms_search/', views.symptoms_search, name='symptoms_search')

]