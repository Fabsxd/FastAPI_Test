from database import Base
from sqlalchemy import Integer, Column, String

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    age = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=False)
    room = Column(Integer, nullable=False)