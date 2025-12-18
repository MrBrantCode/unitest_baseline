"""
QUESTION:
You are given a trapezoid. The lengths of its upper base, lower base, and height are a, b, and h, respectively.
An example of a trapezoid
Find the area of this trapezoid.

-----Constraints-----
 - 1≦a≦100
 - 1≦b≦100
 - 1≦h≦100
 - All input values are integers.
 - h is even.

-----Input-----
The input is given from Standard Input in the following format:
a
b
h

-----Output-----
Print the area of the given trapezoid. It is guaranteed that the area is an integer.

-----Sample Input-----
3
4
2

-----Sample Output-----
7

When the lengths of the upper base, lower base, and height are 3, 4, and 2, respectively, the area of the trapezoid is (3+4)×2/2 = 7.
"""

def calculate_trapezoid_area(a: int, b: int, h: int) -> int:
    """
    Calculate the area of a trapezoid given the lengths of its upper base, lower base, and height.

    Parameters:
    a (int): The length of the upper base.
    b (int): The length of the lower base.
    h (int): The height of the trapezoid.

    Returns:
    int: The area of the trapezoid.
    """
    area = (a + b) * h // 2  # Using integer division to ensure the result is an integer
    return area