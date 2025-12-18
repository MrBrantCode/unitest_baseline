"""
QUESTION:
You are parking at a parking lot. You can choose from the following two fee plans:
 - Plan 1: The fee will be A×T yen (the currency of Japan) when you park for T hours.
 - Plan 2: The fee will be B yen, regardless of the duration.
Find the minimum fee when you park for N hours.

-----Constraints-----
 - 1≤N≤20
 - 1≤A≤100
 - 1≤B≤2000
 - All input values are integers.

-----Input-----
Input is given from Standard Input in the following format:
N A B

-----Output-----
When the minimum fee is x yen, print the value of x.

-----Sample Input-----
7 17 120

-----Sample Output-----
119

 - If you choose Plan 1, the fee will be 7×17=119 yen.
 - If you choose Plan 2, the fee will be 120 yen.
Thus, the minimum fee is 119 yen.
"""

def calculate_minimum_parking_fee(N: int, A: int, B: int) -> int:
    """
    Calculate the minimum parking fee based on the given plans.

    Parameters:
    N (int): The number of hours parked.
    A (int): The fee per hour for Plan 1.
    B (int): The flat fee for Plan 2.

    Returns:
    int: The minimum fee when parked for N hours.
    """
    return min(N * A, B)