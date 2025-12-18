"""
QUESTION:
Create a function called `calculate_circle` that takes a single argument `radius` representing the radius of a circle. The function should calculate and return the area and circumference of the circle rounded to the nearest integer. The input radius must be a positive non-zero number and within the range of 1 to 1000 (inclusive). If the radius is outside this range, the function should return an error message.
"""

def calculate_circle(radius):
    """
    Calculates the area and circumference of a circle given its radius.

    Args:
    radius (float): The radius of the circle.

    Returns:
    str: A string containing the area and circumference of the circle if the radius is valid, otherwise an error message.
    """
    if radius < 1 or radius > 1000:
        return "Radius must be within the range of 1 to 1000 (inclusive)."
    else:
        area = round(3.14159 * radius ** 2)
        circumference = round(2 * 3.14159 * radius)
        return f"Area: {area}\nCircumference: {circumference}"