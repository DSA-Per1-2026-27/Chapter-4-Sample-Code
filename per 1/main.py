from circle import *

def main():
    c = Circle(10)
    print(c)
    # Access a property as if it is an attribute
    print(c.color)
    # Python is designed to avoid getter and setter methods
    # Properties allow you to have all the power of getter
    #   and setter methods without all the boilerplate code

    # c.color = "green" crashes the program
    # This is rude behavior:
    c._color = "green"
    print(c.color)
    # Getting the value of diameter
    print(c.diameter)
    # Setting the value of diameter
    c.diameter = 37
    print(c.radius)

if __name__ == "__main__":
    main()