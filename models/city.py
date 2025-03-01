<<<<<<< HEAD
#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
=======
#!/usr/bin/python3
""" City Module instances cities with ids """
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship

STORAGE = getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """The city class, contains state ID and name"""

    __tablename__ = "cities"
    if STORAGE == "db":
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete-orphan")
    else:
        name = ""
        state_id = ""
>>>>>>> 46a795e91e62913d91cba973594d117f27c00ef5
