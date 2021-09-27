from django.urls import path
from . import views

app_name = "hospital"

urlpatterns = [
    path('all_hospital/', views.all_hospital, name='hospital_list'),
    path('search_hospital', views.search_hospital, name='search_hospital'),
    path('hospital_details/<str:hospital_id>/', views.hospital_details, name='hospital_details'),
]
