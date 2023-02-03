from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

class MovieDirection(Base):

    __tablename__="movie_direction"

    id = Column(Integer, primary_key=True, index=True)
    dir_id = Column(Integer, ForeignKey("dir_id"))
    mov_id = Column(Integer, ForeignKey("mov_id"))
    