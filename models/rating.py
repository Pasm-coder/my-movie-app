from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class Rating(Base):

    __tablename__ = "rating"

    id = Column(Integer, primary_key=True, index=True)
    mov_id = Column(Integer, ForeignKey("mov_id "))
    rev_id = Column(Integer, ForeignKey("rev_id "))
    rev_stars = Column(Integer)
    num_o_ratings = Column(Integer)
