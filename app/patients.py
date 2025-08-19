from sqlalchemy.orm import Session
from app import models, schemas

def create_patient(db: Session, data: schemas.PatientCreate) -> schemas.PatientOut:
    patient = models.Patient(Name=data.name)
    db.add(patient)
    db.commit()
    db.refresh(patient)

    return schemas.PatientOut(
        id=patient.PatientId,
        name=patient.Name,
    )

def list_patients(db: Session) -> list[schemas.PatientOut]:
    patients = db.query(models.Patient).all()
    return [
        schemas.PatientOut(
            id=pt.PatientId,
            name=pt.Name,
        )
        for pt in patients
    ]
