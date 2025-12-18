"""
QUESTION:
Takahashi has a water bottle with the shape of a rectangular prism whose base is a square of side a~\mathrm{cm} and whose height is b~\mathrm{cm}. (The thickness of the bottle can be ignored.)
We will pour x~\mathrm{cm}^3 of water into the bottle, and gradually tilt the bottle around one of the sides of the base.
When will the water be spilled? More formally, find the maximum angle in which we can tilt the bottle without spilling any water.

-----Constraints-----
 - All values in input are integers.
 - 1 \leq a \leq 100
 - 1 \leq b \leq 100
 - 1 \leq x \leq a^2b

-----Input-----
Input is given from Standard Input in the following format:
a b x

-----Output-----
Print the maximum angle in which we can tilt the bottle without spilling any water, in degrees.
Your output will be judged as correct when the absolute or relative error from the judge's output is at most 10^{-6}.

-----Sample Input-----
2 2 4

-----Sample Output-----
45.0000000000

This bottle has a cubic shape, and it is half-full. The water gets spilled when we tilt the bottle more than 45 degrees.
"""

import math

def calculate_max_tilt_angle(a: int, b: int, x: int) -> float:
    """
    Calculate the maximum angle in degrees at which the bottle can be tilted without spilling any water.

    Parameters:
    a (int): The side length of the square base of the bottle in cm.
    b (int): The height of the bottle in cm.
    x (int): The volume of water in the bottle in cm^3.

    Returns:
    float: The maximum angle in degrees at which the bottle can be tilted without spilling any water.
    """
    if a * a * b <= x * 2:
        angle_radians = math.atan(2 * (a * a * b - x) / (a * a * a))
    else:
        angle_radians = math.atan((a * b * b) / (2 * x))
    
    return math.degrees(angle_radians)