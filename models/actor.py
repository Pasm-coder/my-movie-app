from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base


class Actor(Base):

    __tablename__ = "actor"

    act_id = Column(Integer,primary_key = True)
    act_fname = Column(String)
    act_lname = Column(String)
    act_gender = Column(String)

    #movie_casts = relationship("MovieCast", back_populates = "actors")




