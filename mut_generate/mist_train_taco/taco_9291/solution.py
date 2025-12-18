"""
QUESTION:
Takahashi is organizing a party.
At the party, each guest will receive one or more snack pieces.
Takahashi predicts that the number of guests at this party will be A or B.
Find the minimum number of pieces that can be evenly distributed to the guests in both of the cases predicted.
We assume that a piece cannot be divided and distributed to multiple guests.

-----Constraints-----
 - 1 \leq A, B \leq 10^5
 - A \neq B
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
A B

-----Output-----
Print the minimum number of pieces that can be evenly distributed to the guests in both of the cases with A guests and B guests.

-----Sample Input-----
2 3

-----Sample Output-----
6

When we have six snack pieces, each guest can take three pieces if we have two guests, and each guest can take two if we have three guests.
"""

from math import gcd

def minimum_snacks_for_guests(A: int, B: int) -> int:
    """
    Calculate the minimum number of snack pieces that can be evenly distributed
    to the guests in both of the cases predicted by A and B.

    Parameters:
    - A (int): The first predicted number of guests.
    - B (int): The second predicted number of guests.

    Returns:
    - int: The minimum number of snack pieces that can be evenly distributed to both A and B guests.
    """
    lcm = A * B // gcd(A, B)
    return lcm