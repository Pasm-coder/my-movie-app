from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base

class Genres(Base):

    __tablename__ = "genres"

    genres_id = Column(Integer, primary_key=True, index=True)
    genres_title = Column(String)