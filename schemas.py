from pydantic import BaseModel
from datetime import time, datetime
from typing import Optional

#  PATIENTS 
class PatientBase(BaseModel):
    name: str
    age: int
    floor: int
    room: int

class PatientCreate(PatientBase):
    pass  # No incluir 'id' aquí, la base de datos lo genera automáticamente

class Patient(PatientBase):
    id: int

    class Config:
        orm_mode = True

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    floor: Optional[int] = None
    room: Optional[int] = None

#  MEDICINES 
class MedicineBase(BaseModel):
    name: str
    location: str

class MedicineCreate(MedicineBase):
    pass

class Medicine(MedicineBase):
    id: int

    class Config:
        orm_mode = True

#  MEDICINES INVENTORY 
class InventoryBase(BaseModel):
    available_quantity: int
    minimum_quantity: int

class InventoryCreate(InventoryBase):
    medicine_id: int

class Inventory(InventoryBase):
    medicine_id: int

    class Config:
        orm_mode = True

#  PRESCRIPTIONS 
class PrescriptionBase(BaseModel):
    patient_id: int
    medicine_id: int
    pill_per_day: int
    frequency_hr: int

class PrescriptionCreate(PrescriptionBase):
    pass

class Prescription(PrescriptionBase):
    id: int

    class Config:
        orm_mode = True

#  PRESCRIPTION SCHEDULES 
class ScheduleBase(BaseModel):
    hour: time

class ScheduleCreate(ScheduleBase):
    prescription_id: int

class Schedule(ScheduleBase):
    id: int
    prescription_id: int

    class Config:
        orm_mode = True

#  EMERGENCY PRESCRIPTIONS 
class EmergencyBase(BaseModel):
    patient_id: int
    medicine_id: int
    notes: str | None = None

class EmergencyCreate(EmergencyBase):
    pass

class Emergency(EmergencyBase):
    id: int
    datetime: datetime

    class Config:
        orm_mode = True

#  PURCHASE LIST 
class PurchaseBase(BaseModel):
    medicine_id: int
    quantity_needed: int

class PurchaseCreate(PurchaseBase):
    pass

class Purchase(PurchaseBase):
    id: int
    date_needed: datetime

    class Config:
        orm_mode = True
