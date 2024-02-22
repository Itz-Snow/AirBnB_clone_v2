<<<<<<< HEAD
#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
=======
#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship

STORAGE = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = "users"
    if STORAGE == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user", cascade="all, delete-orphan")
        reviews = relationship("Review", backref="user", cascade="all, delete-orphan")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
>>>>>>> 46a795e91e62913d91cba973594d117f27c00ef5
