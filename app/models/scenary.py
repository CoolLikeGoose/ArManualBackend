from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db import Base

class Scenary(Base):
    __tablename__ = "scenarios"
    scenarioID = Column(Integer, primary_key=True, index=True)
    manualID = Column(Integer, ForeignKey("manuals.manualID"), nullable=False, index=True)
    name = Column(String, nullable=False)
    type = Column(Integer, nullable=True)
    category = Column(String, nullable=True)
    note = Column(Text, nullable=True)
    content = Column(Text, nullable=True) 
    order = Column(Integer, nullable=True)

    manual = relationship("Manual", back_populates="scenarios")
    # TODO: link interactions
