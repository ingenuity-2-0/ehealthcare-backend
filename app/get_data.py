from bs4 import BeautifulSoup
import requests
from doctor.models import Specialist, Doctor
from hospital.models import Hospital
from symptoms.models import Symptoms
import json


def data_for_auto_suggestion():
    doctors = Doctor.objects.all()
    doctor_list = []
    for x in doctors:
        doctor_list.append(x.name)
    specialists = Specialist.objects.all()
    for x in specialists:
        doctor_list.append(x.name)
    hospitals = Hospital.objects.all()
    hospital_list = []
    for x in hospitals:
        hospital_list.append(x.name)
    symptoms = Symptoms.objects.all()
    symptom_list = []
    for x in symptoms:
        symptom_list.append(x.symptom)
    with open('./static/assets/dataAPI.json', 'r') as json_file:
        file = json.load(json_file)
        json_file.close()
    file['diseases'] = symptom_list
    file['doctorSpe'] = doctor_list
    file['hospitals'] = hospital_list
    # print(file)
    with open('./static/assets/dataAPI.json', 'w') as json_file:
        json_object = json.dumps(file)
        json_file.write(json_object)
        json_file.close()
    # with open('./data/dataAPI.json', 'w') as json_file:
    # print(doctor_list)
    # print(hospital_list)
    # print(symptom_list)


def covid19_last24():
    url = 'http://103.247.238.92/webportal/pages/covid19.php'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    latest = soup.find_all(class_='callout')
    latest24 = {}
    for x in latest:
        number = x.find(class_="info-box-number")
        number1 = x.find(class_="last_24_hour_body")
        temp1 = str(number1.text.strip())
        temp1 = temp1.replace(' ', '_')
        temp2 = str(number.text.strip())
        latest24.update({temp1: temp2})
    # print(latest24)
    return latest24
