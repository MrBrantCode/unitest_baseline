"""
QUESTION:
Ignoring the air resistance, velocity of a freely falling object $v$ after $t$ seconds and its drop $y$ in $t$ seconds are represented by the following formulas:

$ v = 9.8 t $
$ y = 4.9 t^2 $


A person is trying to drop down a glass ball and check whether it will crack. Your task is to write a program to help this experiment.

You are given the minimum velocity to crack the ball. Your program should print the lowest possible floor of a building to crack the ball. The height of the $N$ floor of the building is defined by $5 \times N - 5$.



Input

The input consists of multiple datasets. Each dataset, a line, consists of the minimum velocity v (0 < v < 200) to crack the ball. The value is given by a decimal fraction, with at most 4 digits after the decimal point. The input ends with EOF. The number of datasets is less than or equal to 50.

Output

For each dataset, print the lowest possible floor where the ball cracks.

Example

Input

25.4
25.4


Output

8
8
"""

import math

def find_lowest_cracking_floor(min_velocity: float) -> int:
    """
    Calculate the lowest possible floor of a building where a glass ball will crack
    given the minimum velocity required to crack the ball.

    The height of the Nth floor of the building is defined by 5 * N - 5.

    Args:
        min_velocity (float): The minimum velocity required to crack the ball.

    Returns:
        int: The lowest possible floor where the ball cracks.
    """
    # Calculate the time required to reach the minimum velocity
    t = min_velocity / 9.8
    
    # Calculate the drop distance in that time
    y = 4.9 * t**2
    
    # Calculate the lowest floor where the drop distance exceeds the height of the floor
    lowest_floor = math.ceil(y / 5) + 1
    
    return lowest_floor