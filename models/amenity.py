#!/usr/bin/python3
"""Esta es la clase de amenidades"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
# from models.place import place_amenity


class Amenity(BaseModel, Base):
    """This is the Amenity class
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    # place_amenities = relationship('Place', secondary='place_amenity')
