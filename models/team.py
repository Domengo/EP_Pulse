from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import Base


class Team(Base):
    """class team

    """
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    city = Column(String)
    players = relationship("Player", back_populates="team")
    coach = relationship("Coach", uselist=False, back_populates="team")
