import unittest
from circle import Circle

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c = Circle(5)
        self.unit = Circle(1)
    
    def test_init(self):
        self.assertIsInstance(self.c, Circle)
        self.assertIsInstance(self.unit, Circle)
    
    def test_str(self):
        self.assertIsInstance(str(self.c), str)
        self.assertEqual(str(self.c), "Circle of radius 5.")
        self.assertEqual(str(self.unit), "Circle of radius 1.")

    def test_repr(self):
        self.assertIsInstance(repr(self.c), str)
        self.assertIsInstance(eval(repr(self.c)), Circle)
        self.assertEqual(eval(repr(self.c)).radius, 5)
        self.assertEqual(repr(self.c), "Circle(5)")
        self.assertEqual(repr(self.unit), "Circle(1)")
    
    def test_color(self):
        # The @property decorator makes the method .color look like an
        #   attribute, you interact with it like an attribute.
        self.assertEqual(self.c.color, "blue")
        self.assertEqual(self.unit.color, "blue")
        # We made .color read-only, so test that it raises an error:
        with self.assertRaises(AttributeError):
            self.c.color = "green"
    
    def test_diameter(self):
        self.assertEqual(self.c.diameter, 10)
        self.assertEqual(self.unit.diameter, 2)
        self.c.diameter = 59
        self.assertAlmostEqual(self.c.radius, 29.5)
        self.assertAlmostEqual(self.c.diameter, 59)