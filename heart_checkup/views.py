from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def heart_checkup(request):
    return render(request, template_name='heart_checkup/heart-checkup.html')


def checkup(request):
    if request.method == 'POST':
        # data = request.POST.dict()
        # print(data)
        sex = request.POST['gender']
        age = request.POST.get('age_1')
        fbs1 = request.POST['fbs']
        hr = request.POST['hr']
        # fbs2 = request.POST['fbs1']
        print(sex)
        print(age)
        print(fbs1)
        print(hr)
    return HttpResponse('testing')
