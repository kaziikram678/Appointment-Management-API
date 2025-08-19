from sqlalchemy.orm import Session
from app import models, schemas

def create_appointment(db: Session, data: schemas.AppointmentCreateIn) -> schemas.AppointmentOut:
    patient = db.query(models.Patient).filter(models.Patient.PatientId == data.PatientId).first()
    if not patient:
        raise ValueError("No patient available of this id")

    appointment = models.Appointment(
        PatientId=data.PatientId,
        AppointmentDate=data.AppointmentDate,
        AppointmentTime=data.AppointmentTime,
        Reason=data.Reason,
    )
    db.add(appointment)
    db.commit()
    db.refresh(appointment)

    return schemas.AppointmentOut(
        AppointmentId=appointment.AppointmentId,
        PatientId=appointment.PatientId,
        AppointmentDate=appointment.AppointmentDate,
        AppointmentTime=appointment.AppointmentTime,
        Reason=appointment.Reason,
        Message="Appointment created"
    )

def list_appointments(db: Session) -> list[schemas.AppointmentOut]:
    appointments = db.query(models.Appointment).all()
    return [
        schemas.AppointmentOut(
            AppointmentId=a.AppointmentId,
            PatientId=a.PatientId,
            AppointmentDate=a.AppointmentDate,
            AppointmentTime=a.AppointmentTime,
            Reason=a.Reason,
            Message="Appointment listed"
        )
        for a in appointments
    ]
