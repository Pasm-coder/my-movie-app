from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

class MovieDirection(Base):

    __tablename__="movie_direction"

    id = Column(Integer, primary_key=True, index=True)
    director_id = Column(Integer, ForeignKey("director.director_id"))
    movie_id = Column(Integer, ForeignKey("movie.id"))
    