from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db import Base

class Manual(Base):
    __tablename__ = "manuals"
    manualID = Column(Integer, primary_key=True, index=True)
    companyID = Column(Integer, ForeignKey("companies.accountID"), nullable=False, index=True)
    name = Column(String, nullable=False)
    status = Column(String, nullable=True)
    trackPoints = Column(Integer, default=0)
    createdDate = Column(DateTime, default=datetime.utcnow)
    updatedDate = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    company = relationship("Company", backref="manuals")
    trackpoints = relationship("TrackPoint", back_populates="manual", cascade="all, delete-orphan")
    scenarios = relationship("Scenary", back_populates="manual", cascade="all, delete-orphan")
