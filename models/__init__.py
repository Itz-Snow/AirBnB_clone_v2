<<<<<<< HEAD
#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
=======
#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

STORAGE = getenv("HBNB_TYPE_STORAGE")

if STORAGE == "db":
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
>>>>>>> 46a795e91e62913d91cba973594d117f27c00ef5
