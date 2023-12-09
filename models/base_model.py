#!/usr/bin/python3
'''contains base class for all project'''

import datetime
import uuid
# from models import storage
# from models.engine.file_storage import storage
import models
# from models.engine import storage


class BaseModel:
    '''defines all common attributes/methods for other classes'''
    def __init__(self, *args, **kwargs):
        '''initiate object with its attributes'''
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''object string representation'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''update the record time'''
        self.updated_at = datetime.datetime.now()
        models.storage.save() 

    def to_dict(self):
        '''dictionary of instantce attribute'''
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy       
