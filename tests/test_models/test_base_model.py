#!/usr/bin/python3
"""test module base_model """

import unittest
from datetime import datetime
from models.base_model import BaseModel

from time import sleep
import models

class test_BaseModel(unittest.TestCase):
    '''tesing BaseModel class via unittest'''

    def test_args(self):
        '''test args in the class with different values'''
        self.assertEqual(BaseModel, type(BaseModel()))
        
        p1 = BaseModel(None)
        self.assertNotIn(None, p1.__dict__.values())

    
    def test_objects_storage(self):
        '''test storage object '''
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id(self):
        '''check unique id values'''
        self.assertEqual(str, type(BaseModel().id))
        
        p1 = BaseModel()
        p2 = BaseModel()
        self.assertNotEqual(p1.id, p2.id)

    def test_created_at(self):
        '''check created_at attribute date'''
        self.assertEqual(datetime, type(BaseModel().created_at))
        
        p1 = BaseModel()
        sleep(1)
        p2 = BaseModel()
        self.assertLess(p1.created_at, p2.created_at)

    def test_updated_at(self):
        '''check updated_at attribute date'''
        self.assertEqual(datetime, type(BaseModel().updated_at))
        
        p1 = BaseModel()
        sleep(1)
        p2 = BaseModel()
        self.assertLess(p1.updated_at, p2.updated_at)



    def test_str(self):
        '''check string reperesntation for object'''
        my_date = datetime.now()
        chk_date = repr(my_date)
        p1 = BaseModel()
        p1.id = "333-4444"
        p1.created_at = p1.updated_at = my_date
        val = p1.__str__()
        self.assertIn("[BaseModel] (333-4444)", val)
        self.assertIn("'id': '333-4444'", val)
        self.assertIn("'created_at': " + chk_date, val)
        self.assertIn("'updated_at': " + chk_date, val)



    def test_kwargs(self):
        '''check parameter **kwargs with various values'''
        my_date = datetime.now()
        str_date = my_date.isoformat()
        p1 = BaseModel(id="333-4444", created_at=str_date, updated_at=str_date)
        self.assertEqual(p1.id, "333-4444")
        self.assertEqual(p1.created_at, my_date)
        self.assertEqual(p1.updated_at, my_date)

        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
