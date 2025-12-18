"""
QUESTION:
Takahashi, who is A years old, is riding a Ferris wheel.
It costs B yen (B is an even number) to ride the Ferris wheel if you are 13 years old or older, but children between 6 and 12 years old (inclusive) can ride it for half the cost, and children who are 5 years old or younger are free of charge. (Yen is the currency of Japan.)
Find the cost of the Ferris wheel for Takahashi.

-----Constraints-----
 - 0 ≤ A ≤ 100
 - 2 ≤ B ≤ 1000
 - B is an even number.

-----Input-----
Input is given from Standard Input in the following format:
A B

-----Output-----
Print the cost of the Ferris wheel for Takahashi.

-----Sample Input-----
30 100

-----Sample Output-----
100

Takahashi is 30 years old now, and the cost of the Ferris wheel is 100 yen.
"""

def calculate_ferris_wheel_cost(A: int, B: int) -> int:
    """
    Calculate the cost of the Ferris wheel for Takahashi based on his age.

    Parameters:
    - A (int): Age of Takahashi.
    - B (int): Cost of the Ferris wheel for adults (even number).

    Returns:
    - int: The cost of the Ferris wheel for Takahashi.
    """
    if A >= 13:
        return B
    elif A > 5:
        return B // 2
    else:
        return 0