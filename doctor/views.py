from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor, Specialist
from hospital.models import Hospital, Works


# Create your views here.
# def name_search(request):
#     if request.method == 'POST':
#         city = request.POST['name_cityField']
#         doctor_or_specialist = request.POST['doctor_or_specialist']
#         print(city)
#         print(doctor_or_specialist)
#         doctors = Doctor.objects.all()
#         print(len(doctors))
#         doctor_list = []
#         for x in doctors:
#             try:
#                 name = x.name
#                 specialist = x.specialist_name
#                 hospital_object = Works.objects.get(doctor_id=x.doctor_id)
#                 city = hospital_object.hospital_id.city
#                 hospital_name = hospital_object.hospital_id.name
#                 temp = {
#                     'doctor_name': name,
#                     'specialist': specialist,
#                     'city': city,
#                     'hospital_name': hospital_name
#                 }
#                 doctor_list.append(temp)
#             except:
#                 continue
#         print(len(doctor_list))
#     return render(request, template_name='doctor/ListOfDoctor.html', context={'context': doctor_list})

def name_search(request):
    if request.method == 'POST':
        city = request.POST['name_cityField']
        doctor_or_specialist = request.POST['doctor_or_specialist']
        print(city)
        print(doctor_or_specialist)
        doctors = Doctor.objects.all()
        # print(len(doctors))
        doctor_list = []
        for x in doctors:
            try:
                name = x.name
                specialist = x.specialist_name
                qualification = x.qualification
                designation = x.designation
                # hospital_object = Works.objects.get(doctor_id=x.doctor_id)
                # city = hospital_object.hospital_id.city
                # hospital_name = hospital_object.hospital_id.name
                temp = {
                    'doctor_name': name,
                    'specialist': specialist,
                    'qualification': qualification,
                    'designation': designation
                    # 'city': city,
                    # 'hospital_name': hospital_name
                }
                doctor_list.append(temp)
            except:
                continue
        print(len(doctor_list))
    return render(request, template_name='doctor/ListOfDoctor.html', context={'context': doctor_list})


def symptoms_search(request):
    if request.method == 'POST':
        data = request.POST['tags2']
        print(data)
    return HttpResponse("testing")
