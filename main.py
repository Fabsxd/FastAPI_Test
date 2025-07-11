#fastapi run main.py 
from typing import Union, Literal
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db, init_db
from models import Patient, Prescription, Medicine, PrescriptionSchedule
from contextlib import asynccontextmanager
from schemas import PatientCreate, PatientUpdate


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
@app.get("/")
def read_root():
    return{"Hello" : "World"}

@app.get("/patient/{patient_id}")
async def read_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@app.post("/patient/")
async def create_patient( new_patient: PatientCreate, db: Session = Depends(get_db)):
    new_patient_db = Patient(**new_patient.model_dump())
    db.add(new_patient_db)
    db.commit()
    db.refresh(new_patient_db)
    print(f"Patient successfully created: {new_patient_db.name} (ID: {new_patient_db.id})")
    return new_patient_db

@app.put("/patient/{patient_id}")
async def update_patient(patient_id: int, updated_patient: PatientCreate, db: Session = Depends(get_db)):
    patient_put = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient_put: 
        raise HTTPException(status_code=404, detail="patient not found")
    data = updated_patient.model_dump()
    patient_put.name = data["name"]
    patient_put.age = data["age"]
    patient_put.floor = data["floor"]
    patient_put.room = data["room"]

    db.commit()
    db.refresh(patient_put)
    return patient_put

@app.patch("/patient/{patient_id}")
async def update_patient_data(patient_id: int, updated_patient: PatientUpdate, db: Session = Depends(get_db)):
    patchData = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patchData:
        raise HTTPException(status_code=404, detail="Patient not found")
    data = updated_patient.model_dump(exclude_unset=True)
    for field, value in data.items():
        setattr(patchData, field, value)

    db.commit()
    db.refresh(patchData)
    print(f"Patient successfully updated. ID: {patchData.id}")
    return patchData