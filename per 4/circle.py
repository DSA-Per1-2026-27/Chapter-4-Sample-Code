import math

class Circle:
    """A simple class for geometric circles."""
    def __init__(self, radius: float):
        self.radius = radius
        # A single underscore before the name means private: intended
        #   for internal use only
        self._color = "blue"

    def __str__(self) -> str:
        return f"Circle of radius {self.radius}."
    
    def __repr__(self) -> str:
        return f"Circle({self.radius})"

    # Case #1 for property decorator:
    # Read-only attribute
    # This example is a little silly
    @property
    def color(self):
        return self._color

    # Case #2 for property decorator:
    # Computed attributes
    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, new_diameter):
        self.radius = new_diameter / 2

    @property
    def area(self) -> float:
        return math.pi * self.radius**2
    
    @property
    def circumference(self) -> float:
        return math.pi * self.diameter