from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.db import Base
from sqlalchemy.orm import relationship

class TrackPoint(Base):
    __tablename__ = "trackpoints"
    trackpointID = Column(Integer, primary_key=True, index=True)
    manualID = Column(Integer, ForeignKey("manuals.manualID"), nullable=False, index=True)
    arucoID = Column(Integer, nullable=True)
    sizeCm = Column(Float, nullable=True)
    trackpointName = Column(String, nullable=True)
    description = Column(String, nullable=True)

    manual = relationship("Manual", back_populates="trackpoints")
    interaction_points = relationship("InteractionPoint", back_populates="trackpoint", cascade="all, delete-orphan")
