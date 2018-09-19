# 4. Write a python program to create the following management systems.
# a. Hospital admission System (e.g. classes Patient, Doctor, Medical Admission Clerk, Book, Nurse,  etc.)
#class Person(object):

class Hospital:
    def __init__(self):
        self.doctor = []
        self.patient = []
        self.nurse = []
        self.calendar = []
        self.book = []

class Patient: # Class Patient
    def __init__(self, fullname, age, address,ssn):
        self.fullname = fullname
        self.age = age
        self.address = address
        self.ssn = ssn

class Doctor: #Class Doctor
    def __init__(self, fullname,specialty, address,snn):
        super(Doctor, self).__init(self, fullname, address,snn)
        self.specialty = specialty
    def Calendar(self, doctor, patien, time):
        self.time = time
        self.doctor = doctor
        self.patient = patient
        if self.doctor.is_available(time) and self.patient.is_available(time):
            self.patient.update_calendar(patient,time)
            self.doctor.update_calendar(doctor, time)
            print("Schedule")
            return True
