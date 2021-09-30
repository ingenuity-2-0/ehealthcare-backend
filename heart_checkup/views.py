from django.shortcuts import render
import joblib
import numpy as np
from doctor.getData import search_doctor_using_name
from django.conf import settings
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='users:login')
def heart_checkup(request):
    return render(request, template_name='heart_checkup/heart-checkup.html')


@login_required(login_url='users:login')
def checkup(request):
    if request.method == 'POST':
        sex = request.POST['gender']
        age = request.POST.get('age_1')
        fbs = request.POST['fbs']
        exang = request.POST['exang']
        restecg = request.POST['restecg']
        trestbps = request.POST['trestbps']
        cp = request.POST['cp']
        thalach = request.POST['thalach']
        thal = request.POST['thal']
        slope = request.POST['slope']
        ca = request.POST['ca']
        chol = request.POST['chol']
        oldpeak = request.POST['oldpeak']
        data = (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
        print(data)
        predict_data = tuple(map(int, data))
        model = joblib.load('data/model (1).sav')
        # change the input data to a numpy array
        predict_data_as_numpy_array = np.asarray(predict_data)

        # reshape the numpy array as we are predicting for only on instance
        predict_data_reshaped = predict_data_as_numpy_array.reshape(1, -1)
        prediction = model.predict(predict_data_reshaped)
        print(prediction)

        if prediction[0] == 0:
            h = 'The Person does not have a Heart Disease'
            doctor_list = search_doctor_using_name(name='Cardiology')
        else:
            h = 'The Person has Heart Disease'
            doctor_list = search_doctor_using_name(name='Medicine')
    return render(request, template_name='doctor/ListOfDoctor.html', context={'context': doctor_list})
