#!/usr/bin/python3
"""test module amenity """

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class test_Review(unittest.TestCase):
    '''tesing Amenity class via unittest'''

    def test_args(self):
        '''test args in the class with different values'''
        self.assertEqual(Review, type(Review()))
    
        p = Review(None)
        self.assertNotIn(None, p.__dict__.values())

    def test_storage(self):
        '''test storage object '''
        self.assertIn(Review(), models.storage.all().values())

    def test_id(self):
        '''check unique id values'''
        self.assertEqual(str, type(Review().id))
        
        p = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(p))
        self.assertNotIn("place_id", p.__dict__)

        p1 = Review()
        p2 = Review()
        self.assertNotEqual(p1.id, p2.id)

    def test_created_at(self):
        '''check created_at attribute date'''
        self.assertEqual(datetime, type(Review().created_at))

        p1 = Review()
        sleep(1)
        p2 = Review()
        self.assertLess(p1.created_at, p2.created_at)
        

    def test_updated_at(self):
        '''check updated_at attribute date'''
        self.assertEqual(datetime, type(Review().updated_at))
        p1 = Review()
        sleep(1)
        p2 = Review()
        self.assertLess(p1.updated_at, p2.updated_at)

    
    def test_text(self):
        '''check text attribute'''
        p = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(p))
        self.assertNotIn("text", p.__dict__)


    def test_str(self):
        '''check string reperesntation for object'''
        my_date = datetime.now()
        chk_date = repr(my_date)
        p1 = Review()
        p1.id = "333-4444"
        p1.created_at = p1.updated_at = my_date
        val = p1.__str__()
        self.assertIn("[Review] (333-4444)", val)
        self.assertIn("'id': '333-4444'", val)
        self.assertIn("'created_at': " + chk_date, val)
        self.assertIn("'updated_at': " + chk_date, val)


    def test_kwargs(self):
        '''check parameter **kwargs with various values'''
        my_date = datetime.now()
        str_date = my_date.isoformat()
        p1 = Review(id="333-4444", created_at=str_date, updated_at=str_date)
        self.assertEqual(p1.id, "333-4444")
        self.assertEqual(p1.created_at, my_date)
        self.assertEqual(p1.updated_at, my_date)
    
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

if __name__ == "__main__":
    unittest.main()
