"""
QUESTION:
Write a simple function that takes polar coordinates (an angle in degrees and a radius) and returns the equivalent cartesian coordinates (rouded to 10 places).

```
For example:

coordinates(90,1)
=> (0.0, 1.0)

coordinates(45, 1)
=> (0.7071067812, 0.7071067812)
```
"""

from math import cos, sin, radians

def polar_to_cartesian(angle_degrees, radius, precision=10):
    """
    Converts polar coordinates (angle in degrees and radius) to cartesian coordinates (x, y).

    Parameters:
    - angle_degrees (float or int): The angle in degrees.
    - radius (float or int): The radius.
    - precision (int, optional): The number of decimal places to round the cartesian coordinates to. Default is 10.

    Returns:
    - tuple: A tuple containing the cartesian coordinates (x, y), both rounded to the specified precision.
    """
    x = radius * cos(radians(angle_degrees))
    y = radius * sin(radians(angle_degrees))
    return (round(x, precision), round(y, precision))