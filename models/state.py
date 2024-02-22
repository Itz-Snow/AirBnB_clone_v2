<<<<<<< HEAD
#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""
=======
#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv

STORAGE = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """State class for the states of a country"""

    __tablename__ = "states"
    if STORAGE == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="states", cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            from models import storage

            list_city = []
            all_ins = storage.all(City)
            for value in all_ins.values():
                if value.state_id == self.id:
                    list_city.append(value)
            return list_city
>>>>>>> 46a795e91e62913d91cba973594d117f27c00ef5
