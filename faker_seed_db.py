from faker import Faker

# Creation of faker profile helper function
def getProfile():
    fake = Faker()
    return fake.profile()

# Gather Data and place inside of database
import os
from flask_api.models import Patient
from flask_api import db

def seedData():
    for seed_num in range(10):
        data = getProfile()
        patient = Patient(
            data['name'], data['sex'], data['address'], data['ssn'],\
            data['blood_group'], data['mail']
        )

        db.session.add(patient)
        db.session.commit()

# seedData() 
# could do and run this program or will put this in app.py through import and only run
# flask run