from circle import Circle

def main():
    c = Circle(5)
    unit = Circle(1)
    print(c)
    print(unit)
    c.diameter = 59
    print(c)
    print(type(c.diameter))
    print(c.area)
    print(c.circumference)
    print(dir(c))

if __name__ == "__main__":
    main()