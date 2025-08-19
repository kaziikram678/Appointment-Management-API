from pydantic import BaseModel

class PatientCreate(BaseModel):
    name: str

class PatientOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class AppointmentCreateIn(BaseModel):
    PatientId: int
    AppointmentDate: str
    AppointmentTime: str
    Reason: str

class AppointmentOut(BaseModel):
    AppointmentId: int
    PatientId: int
    AppointmentDate: str
    AppointmentTime: str
    Reason: str
    Message: str = "Appointment created successfully"

    class Config:
        orm_mode = True
