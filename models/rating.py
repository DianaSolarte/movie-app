from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base
from models.reviewer import Base

class Rating(Base):

    __tablename__ = "rating"

    mov_id = Column(Integer,primary_key = True)
    rev_id = Column(Integer)
    rev_srtars = Column(Integer)
    num_o_ratings = Column(Integer)
