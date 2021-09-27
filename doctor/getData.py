from .models import Doctor, Specialist
from hospital.models import Hospital, Works
from symptoms.models import Symptoms
import ast
from statistics import mode


def all_doctor_info():
    doctors = Doctor.objects.all()
    doctor_list = []
    for x in doctors:
        doctor_id = x.doctor_id
        name = x.name
        specialist = x.specialist_name
        try:
            hospital_object = Works.objects.get(doctor_id=x.doctor_id)
            city = hospital_object.hospital_id.city
            hospital_name = hospital_object.hospital_id.name
            hospital_id = hospital_object.hospital_id.hospital_id
        except:
            city = ''
            hospital_name = ''
            hospital_id = 'NaN'
        temp = {
            'doctor_id': doctor_id,
            'doctor_name': name,
            'specialist': specialist,
            'city': city,
            'hospital_name': hospital_name,
            'hospital_id': hospital_id,
        }
        doctor_list.append(temp)
    return doctor_list


def search_doctor_using_name(name):
    doctors = Doctor.objects.filter(name__iregex=name)
    if len(doctors) == 0:
        doctors = Doctor.objects.filter(specialist_name__name__iregex=name)
    doctor_list = []
    for x in doctors:
        doctor_id = x.doctor_id
        name = x.name
        specialist = x.specialist_name
        try:
            hospital_object = Works.objects.get(doctor_id=x.doctor_id)
            city = hospital_object.hospital_id.city
            hospital_name = hospital_object.hospital_id.name
            hospital_id = hospital_object.hospital_id.hospital_id
        except:
            city = ''
            hospital_name = ''
            hospital_id = 'NaN'
        temp = {
            'doctor_id': doctor_id,
            'doctor_name': name,
            'specialist': specialist,
            'city': city,
            'hospital_name': hospital_name,
            'hospital_id': hospital_id,
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
    # print(specialist_name)
    doctor_list = search_doctor_using_name(specialist_name)
    return doctor_list


def doctor_information(dr_id):
    doctor_object = Doctor.objects.get(doctor_id=dr_id)
    doctor_image = doctor_object.image
    doctor_name = doctor_object.name
    doctor_qualification = doctor_object.qualification
    doctor_designation = doctor_object.designation
    doctor_specialist = doctor_object.specialist_name.name
    doctor_work_objects = Works.objects.filter(doctor_id=dr_id)
    hospital_list = []
    for x in doctor_work_objects:
        hospital_name = x.hospital_id.name
        hospital_address = x.hospital_id.address
        consulting_hour_start = x.start
        consulting_hour_end = x.end
        consulting_days = x.days
        consulting_fees = x.fees
        temp = {
            'hospital_name': hospital_name,
            'hospital_address': hospital_address,
            'consulting_hour_start': consulting_hour_start,
            'consulting_hour_end': consulting_hour_end,
            'consulting_days': consulting_days,
            'consulting_fees': consulting_fees
        }
        hospital_list.append(temp)
    related_doctor_object = Doctor.objects.filter(specialist_name__name__iregex=doctor_specialist)[0:3]
    related_doctor_list = []
    for related in related_doctor_object:
        r_doctor_id = related.doctor_id
        r_doctor_name = related.name
        r_doctor_image = related.image
        r_doctor_specialist = related.specialist_name.name
        temp = {
            'r_doctor_id': r_doctor_id,
            'r_doctor_name': r_doctor_name,
            'r_doctor_image': r_doctor_image,
            'r_doctor_specialist': r_doctor_specialist
        }
        related_doctor_list.append(temp)
    doctor_info = {
        'doctor_name': doctor_name,
        'doctor_image': doctor_image,
        'doctor_qualification': doctor_qualification,
        'doctor_designation': doctor_designation,
        'doctor_specialist': doctor_specialist,
        'works': hospital_list,
        'related_doctors': related_doctor_list
    }
    return doctor_info


