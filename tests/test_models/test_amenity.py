#!/usr/bin/python3
"""test module amenity """



import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    '''tesing Amenity class via unittest'''

    def test_arg(self):
        '''test args in the class with different values'''
        self.assertEqual(Amenity, type(Amenity()))

        p1 = Amenity(None)
        self.assertNotIn(None, p1.__dict__.values())

    def test_storage(self):
        '''test storage object '''
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id(self):
        '''check unique id values'''
        self.assertEqual(str, type(Amenity().id))
        self.assertEqual(datetime, type(Amenity().created_at))
        p1 = Amenity()
        p2 = Amenity()
        self.assertNotEqual(p1.id, p2.id)

    def test_updated(self):
        '''check updated_at attribute date'''
        self.assertEqual(datetime, type(Amenity().updated_at))
        

    def test_name(self):
        '''check name attribute '''
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)



    def test_created_at(self):
        '''check created_at attribute date'''
        p1 = Amenity()
        sleep(1)
        p2 = Amenity()
        self.assertLess(p1.created_at, p2.created_at)

    def test_updated_at(self):
        '''check updated_at attribute date'''
        p1 = Amenity()
        sleep(1)
        p2 = Amenity()
        self.assertLess(p1.updated_at, p2.updated_at)


    def test_str(self):
        '''check string reperesntation for object'''
        my_date = datetime.now()
        chk_date = repr(my_date)
        p1 = Amenity()
        p1.id = "333-4444"
        p1.created_at = p1.updated_at = my_date
        val = p1.__str__()
        self.assertIn("[Amenity] (333-4444)", val)
        self.assertIn("'id': '333-4444'", val)
        self.assertIn("'created_at': " + chk_date, val)
        self.assertIn("'updated_at': " + chk_date, val)   



    def test_kwargs(self):
        '''check parameter **kwargs with various values'''
        my_date = datetime.now()
        str_date = my_date.isoformat()
        p1 = Amenity(id="333-4444", created_at=str_date, updated_at=str_date)
        self.assertEqual(p1.id, "333-4444")
        self.assertEqual(p1.created_at, my_date)
        self.assertEqual(p1.updated_at, my_date)
    
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)




if __name__ == "__main__":
    unittest.main()
