from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Appointment(db.Model):
    __tablename__ = "appointments"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    nic = db.Column(db.String(13), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    appointment_date = db.Column(db.Date, nullable=False)
    department = db.Column(db.String(100), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctor.id"), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    has_visited = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(20), default="Pending")

class Doctor(db.Model):
    __tablename__ = "doctor"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    nic = db.Column(db.String(13), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    avatar_url = db.Column(db.String(255))
    appointments = db.relationship("Appointment", backref="doctor", lazy=True)

class Patient(db.Model):
    __tablename__ = "patients"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    nic = db.Column(db.String(13), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    medical_history = db.relationship("MedicalHistory", backref="patient", lazy=True)
    appointments = db.relationship("Appointment", backref="patient", lazy=True)

class MedicalHistory(db.Model):
    __tablename__ = "medical_history"
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)
    diagnosis = db.Column(db.String(255), nullable=False)
    treatment = db.Column(db.String(255), nullable=False)
    notes = db.Column(db.Text, nullable=True)
    date = db.Column(db.Date, default=datetime.utcnow)

class Staff(db.Model):
    __tablename__ = "staff"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    nic = db.Column(db.String(13), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    role = db.Column(db.String(50), nullable=False)  
    address = db.Column(db.String(255), nullable=False)
