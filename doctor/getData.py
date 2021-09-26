from .models import Doctor, Specialist
from hospital.models import Hospital, Works
from symptoms.models import Symptoms
import ast
from statistics import mode


def all_doctor_info():
    doctors = Doctor.objects.all()
    doctor_list = []
    for x in doctors:
        name = x.name
        specialist = x.specialist_name
        try:
            hospital_object = Works.objects.get(doctor_id=x.doctor_id)
            city = hospital_object.hospital_id.city
            hospital_name = hospital_object.hospital_id.name
        except:
            city = ''
            hospital_name = ''
        temp = {
            'doctor_name': name,
            'specialist': specialist,
            'city': city,
            'hospital_name': hospital_name
        }
        doctor_list.append(temp)
    return doctor_list


def search_doctor_using_name(name):
    doctors = Doctor.objects.filter(name__iregex=name)
    if len(doctors) == 0:
        doctors = Doctor.objects.filter(specialist_name__name__iregex=name)
    doctor_list = []
    for x in doctors:
        name = x.name
        specialist = x.specialist_name
        try:
            hospital_object = Works.objects.get(doctor_id=x.doctor_id)
            city = hospital_object.hospital_id.city
            hospital_name = hospital_object.hospital_id.name
        except:
            city = ''
            hospital_name = ''
        temp = {
            'doctor_name': name,
            'specialist': specialist,
            'city': city,
            'hospital_name': hospital_name
        }
        doctor_list.append(temp)
    return doctor_list


def search_doctor_using_city(city):
    all_doctors = all_doctor_info()
    sorted_doctor_list = []
    for x in all_doctors:
        if x['city'].lower() == city.lower():
            sorted_doctor_list.append(x)
    return sorted_doctor_list


def search_doctor_using_name_city(name, city):
    doctors = search_doctor_using_name(name=name)
    sorted_doctor_list = []
    for x in doctors:
        if x['city'].lower() == city.lower():
            sorted_doctor_list.append(x)
    return sorted_doctor_list


def search_doctor_using_symptoms(data):
    symptoms = ast.literal_eval(data)
    symptoms_list = []
    for x in symptoms:
        temp = x['value']
        symptoms_list.append(temp)
    list_of_specialist = []
    for x in symptoms_list:
        objects = Symptoms.objects.filter(symptom__iregex=x)
        for sp in objects:
            temp = sp.specialist_id
            list_of_specialist.append(temp)
    specialist_id = mode(list_of_specialist)
    specialist = Specialist.objects.get(id=specialist_id)
    specialist_name = specialist.name
    print(specialist_name)
    doctor_list = search_doctor_using_name(specialist_name)
    return doctor_list
