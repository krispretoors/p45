from app import *
from mars_rover import MarsRover
import unittest
from unittest.mock import patch
from unittest import TestCase

class MarsRoverObject(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = "N"

class Directions(object):
    direction_list = ("N","E","S","W")

class Instructions(object):
    instructions = ("L","R","M")

class TestApp(TestCase):

    def test_validate_rover(self):
        mars_rover = [1,1,"N"]
        self.assertEqual(validate_rover(mars_rover), True)

    def test_invalid_rover_direction(self):
        mars_rover = [1,1,"R"]
        self.assertEqual(validate_rover(mars_rover), None)

    def test_validate_left_instructions(self):
        instruction = "L"
        self.assertEqual(validate_instructions(instruction), True)

    def test_invalidate_left_instructions(self):
        instruction = "S"
        self.assertEqual(validate_instructions(instruction), False)


if __name__ == '__main__':
    unittest.main()