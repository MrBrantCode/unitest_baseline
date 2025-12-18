"""
QUESTION:
It’s still hot every day, but September has already come. It’s autumn according to the calendar. Looking around, I see two red dragonflies at rest on the wall in front of me. It’s autumn indeed.

When two red dragonflies’ positional information as measured from the end of the wall is given, make a program to calculate the distance between their heads.



Input

The input is given in the following format.


$x_1$ $x_2$


The input line provides dragonflies’ head positions $x_1$ and $x_2$ ($0 \leq x_1, x_2 \leq 100$) as integers.

Output

Output the distance between the two red dragonflies in a line.

Examples

Input

20 30


Output

10


Input

50 25


Output

25


Input

25 25


Output

0
"""

def calculate_dragonfly_distance(x1: int, x2: int) -> int:
    """
    Calculate the distance between the heads of two dragonflies given their positions.

    Parameters:
    x1 (int): The position of the first dragonfly's head.
    x2 (int): The position of the second dragonfly's head.

    Returns:
    int: The distance between the two dragonflies' heads.
    """
    return abs(x1 - x2)