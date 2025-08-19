from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Patient(Base):
    __tablename__ = "patients"
    PatientId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    appointments = relationship("Appointment", back_populates="patient")


class Appointment(Base):
    __tablename__ = "appointments"
    AppointmentId = Column(Integer, primary_key=True, index=True)
    PatientId = Column(Integer, ForeignKey("patients.PatientId"))
    AppointmentDate = Column(String)
    AppointmentTime = Column(String)
    Reason = Column(String)
    patient = relationship("Patient", back_populates="appointments")
