"""
QUESTION:
Have you ever heard of the unit "○○ tsubo" that expresses the area of ​​land? Since ancient times, one samurai has said the area for making rice to eat in a day.

There is a land of a [m] x b [m]. Enter a and b and create a program that outputs the tsubo area S [tsubo] of the land. 1 tsubo = 3.305785 [m2], and a and b are integers less than or equal to 100.



input


a b


A and b separated by one space are given on one line.

output

Output the tsubo area S in one line. An error of 0.0001 or less is allowed.

Example

Input

15 25


Output

113.437508
"""

def calculate_tsubo_area(a: int, b: int) -> float:
    """
    Calculate the area of a land in tsubo given its dimensions in meters.

    Parameters:
    a (int): The length of the land in meters.
    b (int): The width of the land in meters.

    Returns:
    float: The area of the land in tsubo, with an error of 0.0001 or less.
    """
    s = a * b
    S = s / 3.305785
    return S