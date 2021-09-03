import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ehealthcare.settings')
django.setup()
from doctor.models import Doctor, Specialist
from hospital.models import Hospital, Works
from symptoms.models import Symptoms


def specialist_load():
    df = pd.read_csv('data/specialist.csv')
    for x in df.index:
        # print(df['sp_id'][x])
        # print(df['specialist_name'][x])
        ob = Specialist(id=df['sp_id'][x], name=df['specialist_name'][x])
        ob.save()


def doctor_load():
    df = pd.read_csv('data/doctors.csv')
    for x in df.index:
        # print(df['sp_id'][x])
        # sp = Specialist.objects.get(id=df['sp_id'][x])
        # print(sp.name)
        ob = Doctor(doctor_id=df['d_id'][x],
                    name=df['doctor_name'][x],
                    qualification=df['qualification'][x],
                    designation=df['designation'][x],
                    specialist_name_id=df['sp_id'][x])
        ob.save()


def hospital_load():
    df = pd.read_csv('data/hospitals.csv')
    # print(df.to_string())
    for x in df.index:
        ob = Hospital(hospital_id=df['h_id'][x],
                      name=df['hospital_name'][x],
                      city=df['City'][x],
                      address=df['address'][x],
                      phone=df['contact'][x], )
        ob.save()


def work_load():
    df = pd.read_csv('data/works.csv')
    for x in df.index:
        ob = Works(doctor_id_id=df['d_id'][x],
                   hospital_id_id=df['h_id'][x],
                   start=df['Consulting_hour_start'][x],
                   end=df['Consulting_hour_end'][x],
                   fees=df['Consulting_fees'][x],
                   days=df['Consulting_days'][x], )
        ob.save()


def symptom_load():
    df = pd.read_csv('data/symptoms.csv')
    for x in df.index:
        ob = Symptoms(symptom=df['symptom'][x],
                      specialist_id=df['sp_id'][x],)
        ob.save()

# specialist_load()
# doctor_load()
# hospital_load()
# work_load()
# symptom_load()