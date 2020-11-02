from flask_api import app, db, ma, login_manager

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String, nullable = False)
    gender = db.Column(db.String, nullable = False)
    address = db.Column(db.String, nullable = False)
    ssn = db.Column(db.String, nullable = False)
    blood_type = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)

    def __init__(self, full_name, gender, address, ssn, blood_type, email, id=id):
        self.full_name = full_name
        self.gender = gender
        self.address = address
        self.ssn = ssn
        self.blood_type = blood_type
        self.email = email

    def __repr__(self):
        return f'Patient {self.full_name} has bee added to the database.'