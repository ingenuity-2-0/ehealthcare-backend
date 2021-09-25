from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def name_search(request):
    if request.method == 'POST':
        city = request.POST['name_cityField']
        doctor_or_specialist = request.POST['doctor_or_specialist']
        print(city)
        print(doctor_or_specialist)
    return HttpResponse("testing")


def symptoms_search(request):
    if request.method == 'POST':
        data = request.POST['tags2']
        print(data)
    return HttpResponse("testing")
