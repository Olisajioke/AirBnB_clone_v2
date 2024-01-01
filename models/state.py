#!/usr/bin/python3
""" State Module for HBNB project"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """This is the class for State."""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Retrieve a list of associated City instances."""
        variables = models.storage.all()
        my_lists = []
        my_sum = []
        for values in variables:
            city_info = values.replace('.', ' ')
            city_info = shlex.split(city_info)
            if city_info[0] == 'City':
                my_lists.append(variables[values])
        for my_elements in my_lists:
            if my_elements.state_id == self.id:
                my_sum.append(my_elements)
        return my_sum
