from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Time, Text, func


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    age = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=False)
    room = Column(Integer, nullable=False)

class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    location = Column(String, nullable=False)

class MedicineStock(Base):
    __tablename__ = "medicines_inventory"

    medicine_id = Column(Integer, ForeignKey("medicines.id"), primary_key=True, index=True)
    available_quantity = Column(Integer, nullable=False)
    minimum_quantity = Column(Integer, nullable=False)
    
class Prescription(Base):
    __tablename__ = "prescriptions"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False, index=True)
    medicine_id = Column(Integer, ForeignKey("medicines.id"), nullable=False)
    pill_per_day = Column(Integer, nullable=False)
    frequency_hr = Column(Integer, nullable=False)

class PrescriptionSchedule(Base):
    __tablename__ = "prescription_schedules"

    id = Column(Integer, primary_key=True)
    prescription_id = Column(Integer, ForeignKey("prescriptions.id"), nullable=False, index=True)
    hour = Column(Time, nullable=False)

class EmergencyPrescription(Base):
    __tablename__ = "emergency_prescriptions"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    medicine_id = Column(Integer, ForeignKey("medicines.id"), nullable=False)
    datetime = Column(DateTime, nullable=False, server_default=func.now())
    notes = Column(Text)

class PurchaseList(Base):
    __tablename__ = "purchase_list"

    id = Column(Integer, primary_key=True)
    medicine_id = Column(Integer, ForeignKey("medicines.id"), nullable=False)
    date_needed = Column(DateTime, nullable=False, server_default=func.now())
    quantity_needed = Column(Integer, nullable=False)
