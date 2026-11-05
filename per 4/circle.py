class Circle:
    """A simple class for geometric circles."""
    # Class attributes are assigned inside the class, but outside
    #   all the methods.
    # Every instance inherits its own copy of the class attribute
    # The instance attribute can be changed without changing the
    #   the class attribute.
    pi = 3.1415926535897932384626433832795

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

    # Be careful about whether you are using the class attribute or
    #   the version that is local to your instance.
    @property
    def area(self) -> float:
        return __class__.pi * self.radius**2
    
    @property
    def circumference(self) -> float:
        return self.pi * self.diameter

    # Case #3 for property decorator
    # Input/Data Validation
    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, new_radius: float) -> None:
        if not (isinstance(new_radius, float) or 
                isinstance(new_radius, int)):
            msg = "Radius has gotta be a real number."
            raise TypeError(msg)
        if new_radius < 0:
            msg = "Negative radius will implode the universe. "
            msg += "Bad vibes."
            raise ValueError(msg)
        self._radius = new_radius

    # Another decorator: @classmethod
    # A common use case for @classmethod is to make an alternate 
    #   constructor.
    @classmethod
    def from_diameter(cls, diameter: float) -> "Circle":
        return Circle(diameter / 2)

    # Another example of class attributes/methods:
    # I had a class that represented the motors on a robot.  Each 
    #   motor was a separate instance of that Motor class.  Then, 
    #   I kept a class attribute that was a list of all instances,
    #   and then I could, say, reset all the motors at once using 
    #   a @classmethod.