from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base_model import Base


class Coach(Base):

    __tablename__ = "coaches"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    team_id = Column(Integer, ForeignKey("teams.id"))
    team = relationship("Team", back_populates="coach")
