"""
QUESTION:
There is a farm whose length and width are A yard and B yard, respectively. A farmer, John, made a vertical road and a horizontal road inside the farm from one border to another, as shown below: (The gray part represents the roads.)

What is the area of this yard excluding the roads? Find it.

-----Note-----
It can be proved that the positions of the roads do not affect the area.

-----Constraints-----
 - A is an integer between 2 and 100 (inclusive).
 - B is an integer between 2 and 100 (inclusive).

-----Input-----
Input is given from Standard Input in the following format:
A B

-----Output-----
Print the area of this yard excluding the roads (in square yards).

-----Sample Input-----
2 2

-----Sample Output-----
1

In this case, the area is 1 square yard.
"""

def calculate_yard_area_excluding_roads(A: int, B: int) -> int:
    """
    Calculate the area of the yard excluding the roads.

    Parameters:
    - A (int): The length of the farm in yards.
    - B (int): The width of the farm in yards.

    Returns:
    - int: The area of the yard excluding the roads in square yards.
    """
    return A * B - B - A + 1