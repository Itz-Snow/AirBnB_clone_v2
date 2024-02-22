<<<<<<< HEAD
#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""
=======
#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship

STORAGE = getenv("HBNB_TYPE_STORAGE")


class Review(BaseModel, Base):
    """Review class to store review information"""

    __tablename__ = "reviews"
    if STORAGE == "db":
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)

    else:
        place_id = ""
        user_id = ""
        text = ""
>>>>>>> 46a795e91e62913d91cba973594d117f27c00ef5
