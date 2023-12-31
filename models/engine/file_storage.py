#!/usr/bin/python3
'''contains FileStorage class for files storage '''

import os
import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review




class FileStorage:
    '''serializes instances to a JSON file and deserializes JSON file to instances'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects
    
    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = obj.__class__.__name__ + "." + obj.id
        # self.__objects[key] = obj.to_dict()
        self.__objects[key] = obj

    
    def save(self):
        '''serializes __objects to the JSON file'''
        glbl_dict = self.__objects
        glbl_dict = {key: glbl_dict[key].to_dict() for key in glbl_dict.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(glbl_dict, f)

    
    def reload(self):
        '''deserializes the JSON file to __objects'''
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name = value["__class__"]
                    cls = eval(cls_name)
                    self.__objects[key] = cls(**value)

