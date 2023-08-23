#!/usr/bin/python3
"""Unit test for State Module """

from tests.test_models.test_base_model import test_basemodel
from models.state import State
import os

class test_state(test_basemodel):
    """ Test for State class"""

    def __init__(self, *args, **kwargs):
        """Test init class"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test for state name"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
