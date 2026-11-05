import unittest
from circle import *

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c = Circle(5)
        self.unit_circle = Circle(1)
    
    def test_init(self):
        self.assertEqual(self.c.radius, 5)
        self.assertEqual(self.unit_circle.radius, 1)

    def test_str(self):
        self.assertIsInstance(str(self.c), str)
        self.assertEqual(str(self.c), 
                "Circle with a radius of 5.")
        self.assertEqual(str(self.unit_circle), 
                "Circle with a radius of 1.")
            
    def test_repr(self):
        self.assertIsInstance(repr(self.c), str)
        self.assertIsInstance(eval(repr(self.c)), Circle)
        self.assertEqual(repr(self.c), "Circle(5)")
        self.assertEqual(repr(self.unit_circle), 
                "Circle(1)")
        self.assertEqual(eval(repr(self.c)).radius, 
                self.c.radius)
    
    def test_color(self):
        self.assertEqual(self.c.color, "blue")
        self.assertEqual(self.unit_circle.color, "blue")
        # color is a read-only property
        with self.assertRaises(AttributeError):
            self.c.color = "green"

    def test_diameter(self):
        self.assertEqual(self.c.diameter, 10)
        self.assertEqual(self.unit_circle.diameter, 2)

    def test_area(self):
        self.assertAlmostEqual(self.c.area, 78.5398, 3)
        self.assertAlmostEqual(self.unit_circle.area, 
                3.14159265358979323, 10)

    def test_radius(self):
        with self.assertRaises(TypeError):
            self.c.radius = ["Tejas", "Kai"]
        with self.assertRaises(ValueError):
            self.c.radius = -1
            