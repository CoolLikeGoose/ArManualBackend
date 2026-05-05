from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.db import Base

class Company(Base):
    __tablename__ = "companies"
    accountID = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    industry = Column(String, nullable=True)
    email = Column(String, nullable=True)
    createdDate = Column(DateTime, default=datetime.utcnow)
    updatedDate = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
