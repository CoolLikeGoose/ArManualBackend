from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db import Base

class InteractionPoint(Base):
    __tablename__ = "interactionpoints"
    interactionPointID = Column(Integer, primary_key=True, index=True)
    trackpointID = Column(Integer, ForeignKey("trackpoints.trackpointID"), nullable=False, index=True)
    position = Column(Text, nullable=True)
    content = Column(Text, nullable=True)

    trackpoint = relationship("TrackPoint", back_populates="interaction_points")
