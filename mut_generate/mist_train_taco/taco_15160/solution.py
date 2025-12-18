"""
QUESTION:
We have two bottles for holding water.
Bottle 1 can hold up to A milliliters of water, and now it contains B milliliters of water.
Bottle 2 contains C milliliters of water.
We will transfer water from Bottle 2 to Bottle 1 as much as possible.
How much amount of water will remain in Bottle 2?

-----Constraints-----
 - All values in input are integers.
 - 1 \leq B \leq A \leq 20
 - 1 \leq C \leq 20

-----Input-----
Input is given from Standard Input in the following format:
A B C

-----Output-----
Print the integer representing the amount of water, in milliliters, that will remain in Bottle 2.

-----Sample Input-----
6 4 3

-----Sample Output-----
1

We will transfer two milliliters of water from Bottle 2 to Bottle 1, and one milliliter of water will remain in Bottle 2.
"""

def calculate_remaining_water(A: int, B: int, C: int) -> int:
    """
    Calculate the amount of water remaining in Bottle 2 after transferring as much water as possible to Bottle 1.

    Parameters:
    - A (int): Maximum capacity of Bottle 1.
    - B (int): Current amount of water in Bottle 1.
    - C (int): Current amount of water in Bottle 2.

    Returns:
    - int: The amount of water remaining in Bottle 2.
    """
    return max(0, C - (A - B))