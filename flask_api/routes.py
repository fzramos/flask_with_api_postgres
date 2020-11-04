from flask_api import app, db
from flask_api.models import Patient, patient_schema, patients_schema
from flask import jsonify, request, render_template

# Endpoint for Creating patients
@app.route('/patients/create', methods = ['POST'])
def create_patient():
    # here we are going to parse input from json style file
    # rather than a formas we did before
    name = request.json['full_name']
    gender = request.json['gender']
    # similar to how we used form.name.data
    address = request.json['address']
    ssn = request.json['ssn']
    blood_type = request.json['blood_type']
    email = request.json['email']

    # adding to model
    patient = Patient(name, gender, address, ssn, blood_type, email)

    # adding to database
    db.session.add(patient)
    db.session.commit()

    # looking at db and checking that requested information was added to the database
    results = patient_schema.dump(patient)
    # Marshmellow patient_schema is a Front End digestible version of the raw db output
    return jsonify(results)


# Endpoint for ALL patients
@app.route('/patients', methods = ['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify(patients_schema.dump(patients))

# Endpoint for ONE patient based on their ID
@app.route('/patients/<id>', methods = ['GET'])
def get_patient(id):
    patient = Patient.query.get(id)
    results = patient_schema.dump(patient)
    return jsonify(results)

# Endpoint for updating patient data
@app.route('/patients/update/<id>', methods = ['POST', 'PUT'])
def update_patients(id):
    patient = Patient.query.get(id)

    # Update info below
    patient.full_name = request.json['full_name']
    patient.gender = request.json['gender']
    patient.address = request.json['address']
    patient.ssn = request.json['ssn']
    patient.blood_type = request.json['blood_type']
    patient.email = request.json['email']

    db.session.commit()

    return patient_schema.jsonify(patient)

# Endpoint for deleting patient data
@app.route('/patients/delete/<id>', methods = ['DELETE'])
def delete_patients(id):
    patient = Patient.query.get(id)

    db.session.delete(patient)
    db.session.commit()

    result = patient_schema.dump(patient)

    return jsonify(result)
