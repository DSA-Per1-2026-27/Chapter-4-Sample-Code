import math

class Circle:
    def __init__(self, radius: float):
        self.radius: float = radius
        self._color = "blue"

    def __str__(self) -> str:
        return f"Circle with a radius of {self.radius}."

    def __repr__(self) -> str:
        return f"Circle({self.radius})"

    # A little silly
    # Use #1 of the @property decorator
    # Make a read-only attribute
    @property
    def color(self) -> str:
        return self._color

    # Use #2: Computed attributes
    @property
    def diameter(self) -> float:
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, new_diameter: float) -> None:
        self.radius = new_diameter / 2

    @property
    def area(self) -> float:
        return math.pi * self.radius**2