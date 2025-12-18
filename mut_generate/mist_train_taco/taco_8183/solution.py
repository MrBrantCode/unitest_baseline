"""
QUESTION:
There is a right triangle ABC with ∠ABC=90°.
Given the lengths of the three sides, |AB|,|BC| and |CA|, find the area of the right triangle ABC.
It is guaranteed that the area of the triangle ABC is an integer.

-----Constraints-----
 - 1 \leq |AB|,|BC|,|CA| \leq 100
 - All values in input are integers.
 - The area of the triangle ABC is an integer.

-----Input-----
Input is given from Standard Input in the following format:
|AB| |BC| |CA|

-----Output-----
Print the area of the triangle ABC.

-----Sample Input-----
3 4 5

-----Sample Output-----
6


This triangle has an area of 6.
"""

def calculate_right_triangle_area(AB: int, BC: int, CA: int) -> int:
    """
    Calculate the area of a right triangle given the lengths of its three sides.

    Parameters:
    - AB (int): The length of side AB.
    - BC (int): The length of side BC.
    - CA (int): The length of side CA.

    Returns:
    - int: The area of the right triangle.
    """
    # Since it's a right triangle, the area can be calculated using the formula:
    # Area = (base * height) / 2
    # Here, we assume AB and BC are the legs of the triangle.
    return int(AB * BC / 2)