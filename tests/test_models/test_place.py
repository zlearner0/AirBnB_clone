#!/usr/bin/python3
"""test module place """

import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class test_Place(unittest.TestCase):
    '''tesing Amenity class via unittest'''

    def test_args(self):
        '''test args in the class with different values'''
        self.assertEqual(Place, type(Place()))

        p = Place(None)
        self.assertNotIn(None, p.__dict__.values())

    def test_storage(self):
        '''test storage object '''
        self.assertIn(Place(), models.storage.all().values())

    def test_id(self):
        '''check unique id values'''
        self.assertEqual(str, type(Place().id))

    def test_created_at(self):
        '''check created_at attribute date'''
        self.assertEqual(datetime, type(Place().created_at))

        p1 = Place()
        sleep(1)
        p2 = Place()
        self.assertLess(p1.created_at, p2.created_at)

    def test_updated_at_(self):
        '''check created_at attribute date'''
        self.assertEqual(datetime, type(Place().updated_at))

    def test_id_(self):
        '''check unique id values'''
        p = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(p))
        self.assertNotIn("city_id", p.__dict__)

        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)



    def test_name(self):
        '''check name attribute '''
        p = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(p))
        self.assertNotIn("name", p.__dict__)

    def test_description(self):
        '''check description attribute '''

        p = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(p))
        self.assertNotIn("desctiption", p.__dict__)

    def test_number_rooms(self):
        '''check rooms no. attribute '''
        p = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(p))
        self.assertNotIn("number_rooms", p.__dict__)

    def test_number_bathrooms(self):
        '''check bath rooms attribute '''
        p = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(p))
        self.assertNotIn("number_bathrooms", p.__dict__)

    def test_max_guest(self):
        '''check guest max attribute '''
        p = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(p))
        self.assertNotIn("max_guest", p.__dict__)

    def test_price_by_night(self):
        '''check price per night attribute '''
        p = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(p))
        self.assertNotIn("price_by_night", p.__dict__)

    def test_latitude(self):
        '''check latitude attribute '''
        p = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(p))
        self.assertNotIn("latitude", p.__dict__)

    def test_longitude(self):
        '''check longitude attribute '''
        p = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(p))
        self.assertNotIn("longitude", p.__dict__)

    def test_amenity_ids(self):
        '''check amenity id attribute '''
        p = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(p))
        self.assertNotIn("amenity_ids", p.__dict__)

    def test_updated_at(self):
        '''check updated_at attribute date'''
        p1 = Place()
        sleep(1)
        p2 = Place()
        self.assertLess(p1.updated_at, p2.updated_at)


    def test_str(self):
        '''check string reperesntation for object'''
        my_date = datetime.now()
        chk_date = repr(my_date)
        p1 = Place()
        p1.id = "333-4444"
        p1.created_at = p1.updated_at = my_date
        val = p1.__str__()
        self.assertIn("[Place] (333-4444)", val)
        self.assertIn("'id': '333-4444'", val)
        self.assertIn("'created_at': " + chk_date, val)
        self.assertIn("'updated_at': " + chk_date, val)   


def test_kwargs(self):
    '''check parameter **kwargs with various values'''
    my_date = datetime.now()
    str_date = my_date.isoformat()
    p1 = Place(id="333-4444", created_at=str_date, updated_at=str_date)
    self.assertEqual(p1.id, "333-4444")
    self.assertEqual(p1.created_at, my_date)
    self.assertEqual(p1.updated_at, my_date)

    with self.assertRaises(TypeError):
        Place(id=None, created_at=None, updated_at=None)



if __name__ == "__main__":
    unittest.main()
