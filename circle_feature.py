import math


def circle(radius):
    """Calculate are and circumference of a circle with a radius"""

    return math.pi*radius**2, 2*math.pi*radius 


def print_circle_features(x):
    """Print the features of a circle"""

    print(f'The area and circumeference of a circle with {x} cm radius \
          are {circle(x)[0]:.2f} cm squared and {circle(x)[0]:.3f}cm. ')
    

if __name__=='__main__':
    print_circle_features(5)
    print()
    print("if works!")