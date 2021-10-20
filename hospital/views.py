from django.shortcuts import render
from .models import Hospital
from .get_data import all_hospital_information, extract_information, hospital_details_information


# Create your views here.
def all_hospital(request):
    hospital_list = all_hospital_information()
    number_of_hospital = len(hospital_list)
    message = 'We get <strong style="color: #be2323" >' + str(number_of_hospital) + '</strong> hospitals for you.'
    return render(request, template_name='hospital/ListOfHospital.html', context={'message': message, 'context': hospital_list})


def search_hospital(request):
    if request.method == 'POST':
        city = request.POST['d_city']
        hospital_name = request.POST['d_name']
        if len(city) != 0 and len(hospital_name) != 0:
            hospitals = Hospital.objects.filter(name__iregex=hospital_name, city__iregex=city)
            hospital_list = extract_information(hospitals)
        elif len(city) == 0 and len(hospital_name) != 0:
            hospitals = Hospital.objects.filter(name__iregex=hospital_name)
            hospital_list = extract_information(hospitals)
        elif len(city) != 0 and len(hospital_name) == 0:
            hospitals = Hospital.objects.filter(city__iregex=city)
            hospital_list = extract_information(hospitals)
        else:
            hospital_list = all_hospital_information()

    number_of_hospital = len(hospital_list)
    message = 'We get <strong style="color: #be2323" >' + str(number_of_hospital) + '</strong> hospitals for you.'
    return render(request, template_name='hospital/ListOfHospital.html', context={'message': message, 'context': hospital_list})


def hospital_details(request, hospital_id):
    hospital_info = hospital_details_information(hospital_id)

    return render(request, template_name='hospital/HospitalProfile.html', context=hospital_info)
