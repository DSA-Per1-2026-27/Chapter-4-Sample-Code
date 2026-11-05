import pickle
import atexit
from circle import *

# Complication with atexit: it can only read global data.
@atexit.register
def save():
    with open("circles.dat", "bw") as f:
        # Notice b=binary which is why I use .dat instead of .txt
        pickle.dump(circles, f)

if __name__ == "__main__":
    with open("circles.dat", "br") as f:
        circles = pickle.load(f)
    print(f"Starting with:\n{circles}")
    rad = True
    while rad:
        rad = input("Give me a new circle radius: ")
        if len(rad) > 0:
            circles.append(Circle(float(rad)))
        print(circles)
