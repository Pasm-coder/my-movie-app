from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class Reviewer(Base):

    __tablename__ = "reviewer"

    id = Column(Integer, primary_key=True, index=True)
    rev_id = Column(Integer, ForeignKey("rating.rev_id"))
    rev_name = Column(String)

