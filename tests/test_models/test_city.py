#!/usr/bin/python3
"""test module city module """

import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class test_City(unittest.TestCase):
    '''tesing City class via unittest'''

    def test_args(self):
        '''test args in the class with different values'''
        self.assertEqual(City, type(City()))

        p1 = City(None)
        self.assertNotIn(None, p1.__dict__.values())

    def test_storage(self):
        '''test storage object '''
        self.assertIn(City(), models.storage.all().values())

    def test_id(self):
        '''check unique id values'''
        self.assertEqual(str, type(City().id))

    def test_created_at(self):
        '''check created_at attribute date'''
        self.assertEqual(datetime, type(City().created_at))

        p1 = City()
        sleep(0.05)
        p2 = City()
        self.assertLess(p1.created_at, p2.created_at)

    def test_updated_at(self):
        '''check updated_at attribute date'''
        self.assertEqual(datetime, type(City().updated_at))
        
        p1 = City()
        sleep(0.05)
        p2 = City()
        self.assertLess(p1.updated_at, p2.updated_at)

        p1 = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(p1))
        self.assertNotIn("state_id", p1.__dict__)
    

    def test_name(self):
        '''check name attribute date'''

        p1 = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(p1))
        self.assertNotIn("name", p1.__dict__)
    
    def test_ids(self):
        '''check unique id values'''
        p1 = City()
        p2 = City()
        self.assertNotEqual(p1.id, p2.id)        




    def test_str(self):
        '''check string reperesntation for object'''
        my_date = datetime.now()
        chk_date = repr(my_date)
        p1 = City()
        p1.id = "333-4444"
        p1.created_at = p1.updated_at = my_date
        val = p1.__str__()
        self.assertIn("[City] (333-4444)", val)
        self.assertIn("'id': '333-4444'", val)
        self.assertIn("'created_at': " + chk_date, val)
        self.assertIn("'updated_at': " + chk_date, val) 
        
    
    def test_kwargs(self):
        '''check parameter **kwargs with various values'''
        my_date = datetime.now()
        str_date = my_date.isoformat()
        p1 = City(id="333-4444", created_at=str_date, updated_at=str_date)
        self.assertEqual(p1.id, "333-4444")
        self.assertEqual(p1.created_at, my_date)
        self.assertEqual(p1.updated_at, my_date)
    
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
