from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

class MovieGenres(Base):

    __tablename__="movie_genres"
    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movie.id"))
    gen_id = Column(Integer, ForeignKey("genres.genres_id"))
    