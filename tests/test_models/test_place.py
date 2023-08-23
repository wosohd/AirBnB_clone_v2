#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import os


class test_Place(test_basemodel):
    """ place tests class"""

    def __init__(self, *args, **kwargs):
        """ init test"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ place city_id attr"""
        new = self.value()
        self.assertEqual(type(new.city_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_user_id(self):
        """ place user_id attr"""
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_name(self):
        """place name attr"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_description(self):
        """description attr"""
        new = self.value()
        self.assertEqual(type(new.description), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_number_rooms(self):
        """number of rooms attr"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_number_bathrooms(self):
        """number of bathrooms attr"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_max_guest(self):
        """max_guest attr"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_price_by_night(self):
        """price by night attr"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_latitude(self):
        """Latitude attr"""
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_longitude(self):
        """longitude attr"""
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_amenity_ids(self):
        """amenity ids"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
