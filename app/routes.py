from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import PatientCreate, PatientOut, AppointmentCreateIn, AppointmentOut
from app import patients, appointments

router = APIRouter(tags=["API"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/patients/", response_model=PatientOut)
def create_patient(payload: PatientCreate, db: Session = Depends(get_db)):
    return patients.create_patient(db, payload)

@router.get("/patients/", response_model=list[PatientOut])
def get_patients(db: Session = Depends(get_db)):
    return patients.list_patients(db)

@router.post("/appointments/", response_model=AppointmentOut)
def create_appointment(payload: AppointmentCreateIn, db: Session = Depends(get_db)):
    try:
        return appointments.create_appointment(db, payload)
    except ValueError as e:
        raise HTTPException(status_code=400)

@router.get("/appointments/", response_model=list[AppointmentOut])
def get_appointments(db: Session = Depends(get_db)):
    return appointments.list_appointments(db)
