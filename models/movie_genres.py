from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

class MovieGenres(Base):

    __tablename__="movie_genres"
    
    movie_id = Column(Integer, ForeignKey("movie_id"))
    gen_id = Column(Integer, ForeignKey("actor_id"))
    