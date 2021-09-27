from django.shortcuts import render
from django.http import HttpResponse
from .get_data import data_for_auto_suggestion, covid19_last24, covid19_api
from django.views.decorators.clickjacking import xframe_options_exempt


# Create your views here.
def home(request):
    latest24 = covid19_last24()
    return render(request, template_name='app/index.html', context={'context': latest24})


def test(request):
    data_for_auto_suggestion()
    return HttpResponse('Hello world')


@xframe_options_exempt
def covid19(request):
    covid_data = covid19_api()
    return render(request, template_name='app/covid.html', context=covid_data)
