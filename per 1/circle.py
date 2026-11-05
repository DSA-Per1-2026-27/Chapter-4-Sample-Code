import math

class Circle:
    # Class attribute, just define it outside any method.
    # Politeness dictates that you should do this up top.
    pi = 3.1415926535897932384626433832795

    """When you have a class attribute, each instance gets its own copy
    of that attribute.  HOWEVER, each instance can set its own value for 
    that attribute, it CAN be changed.
    """

    def __init__(self, radius: float):
        # This next line calls the .setter method
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
        # I can access the class attribute pi using __class__:
        return __class__.pi * self.radius**2

    @property
    def circumference(self) -> float:
        # And I can access the class attribute using self also:
        return self.pi * self.diameter

    # Use #3 of @property: Input validation
    @property
    def radius(self) -> float | int:
        return self._radius
    
    @radius.setter
    def radius(self, new_radius: float | int) -> None:
        if not (isinstance(new_radius, int) or 
                isinstance(new_radius, float)):
            msg = "Radius is a number.  Or a bone, but not this radius."
            raise TypeError(msg)
        if new_radius < 0:
            msg = "Negative radius will implode the universe. "
            msg += "Bad vibes."
            raise ValueError(msg)
        self._radius = new_radius

    # New decorator. Most common use is to create an alternate constructor
    @classmethod
    def from_diameter(cls, new_diameter: float | int) -> "Circle":
        return Circle(new_diameter / 2)

    # Another example of a use for @classmethod:
    """I once had a class that represented the motors on a robot.  Each
    motor was one instance of that class.

    I used a @classmethod to reset all the motors.

    In any case, a @classmethod is an action that applies to the entire
    category not just a single instance.
    """