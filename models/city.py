#!/usr/bin/python3
'''contains City class for AirBnb'''
from models.base_model import BaseModel


class City(BaseModel):
    '''inherits from BaseModel'''
    state_id = ""
    name = ""
