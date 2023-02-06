from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base

class Director(Base):

    __tablename__ = "director"

    director_id = Column(Integer,primary_key = True)
    director_fname = Column(String)
    director_lname = Column(String)