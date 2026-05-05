from sqlalchemy import Column, Integer, ForeignKey, Text, PrimaryKeyConstraint
from app.db import Base

class ScenarioInteraction(Base):
    __tablename__ = "scenario_interactions"
    # TODO: add interaction id?
    scenarioID = Column(Integer, ForeignKey("scenarios.scenarioID"), nullable=False)
    interactionPointID = Column(Integer, ForeignKey("interactionpoints.interactionPointID"), nullable=False)
    overrideContent = Column(Text, nullable=True)  # JSON
    order = Column(Integer, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('scenarioID', 'interactionPointID', name='pk_scenario_interaction'),
    )
