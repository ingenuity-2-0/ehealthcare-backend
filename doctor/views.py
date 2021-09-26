from django.shortcuts import render
from .getData import all_doctor_info, search_doctor_using_name, search_doctor_using_city, \
search_doctor_using_name_city, search_doctor_using_symptoms


# Create your views here.
def name_search(request):
    if request.method == 'POST':
        city = request.POST['name_cityField']
        doctor_or_specialist = request.POST['doctor_or_specialist']
        if len(city) != 0 and len(doctor_or_specialist) != 0:
            doctor_list = search_doctor_using_name_city(name=doctor_or_specialist, city=city)
        elif len(city) == 0 and len(doctor_or_specialist) != 0:
            doctor_list = search_doctor_using_name(name=doctor_or_specialist)
        elif len(city) != 0 and len(doctor_or_specialist) == 0:
            doctor_list = search_doctor_using_city(city=city)
        else:
            doctor_list = all_doctor_info()
    return render(request, template_name='doctor/ListOfDoctor.html', context={'context': doctor_list})


def symptoms_search(request):
    if request.method == 'POST':
        data = request.POST['tags2']
        doctor_list = search_doctor_using_symptoms(data)
    return render(request, template_name='doctor/ListOfDoctor.html', context={'context': doctor_list})


def all_doctor(request):
    doctor_list = all_doctor_info()
    return render(request, template_name='doctor/ListOfDoctor.html', context={'context': doctor_list})
