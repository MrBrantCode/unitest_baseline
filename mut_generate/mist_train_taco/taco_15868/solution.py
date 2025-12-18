"""
QUESTION:
Given is a positive integer L.
Find the maximum possible volume of a rectangular cuboid whose sum of the dimensions (not necessarily integers) is L.

-----Constraints-----
 - 1 ≤ L ≤ 1000
 - L is an integer.

-----Input-----
Input is given from Standard Input in the following format:
L

-----Output-----
Print the maximum possible volume of a rectangular cuboid whose sum of the dimensions (not necessarily integers) is L.
Your output is considered correct if its absolute or relative error from our answer is at most 10^{-6}.

-----Sample Input-----
3

-----Sample Output-----
1.000000000000

For example, a rectangular cuboid whose dimensions are 0.8, 1, and 1.2 has a volume of 0.96.
On the other hand, if the dimensions are 1, 1, and 1, the volume of the rectangular cuboid is 1, which is greater.
"""

def max_cuboid_volume(L: int) -> float:
    """
    Calculate the maximum possible volume of a rectangular cuboid whose sum of the dimensions is L.

    Parameters:
    L (int): The sum of the dimensions of the rectangular cuboid.

    Returns:
    float: The maximum possible volume of the rectangular cuboid.
    """
    A = L / 3
    return A * A * A