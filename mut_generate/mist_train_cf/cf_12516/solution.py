"""
QUESTION:
Create a function `calculate_surface_area` that calculates the surface area of a cylinder given its radius and height, without using the built-in mathematical functions such as pi. The function should only use basic mathematical operations and handle both positive and negative values for radius and height inputs. The function should also round the surface area to 2 decimal places.
"""

def calculate_surface_area(radius, height):
    # Calculate the surface area of the top and bottom circles
    circle_area = 3.14 * 2 * radius * radius

    # Calculate the surface area of the side of the cylinder
    side_area = 2 * 3.14 * radius * height

    # Calculate the total surface area
    surface_area = circle_area + side_area

    return round(surface_area, 2)