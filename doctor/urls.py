from django.urls import path
from . import views

app_name = "doctor"

urlpatterns = [
    path('name_search/', views.name_search, name='name_search'),
    path('symptoms_search/', views.symptoms_search, name='symptoms_search'),
    path('all_doctor_list/', views.all_doctor, name='all_doctor_list'),
    path('details/<str:doctor_id>/', views.doctor_details, name='doctor_detail')

]
