"""
QUESTION:
We have a sandglass that runs for X seconds. The sand drops from the upper bulb at a rate of 1 gram per second. That is, the upper bulb initially contains X grams of sand.
How many grams of sand will the upper bulb contains after t seconds?

-----Constraints-----
 - 1≤X≤10^9
 - 1≤t≤10^9
 - X and t are integers.

-----Input-----
The input is given from Standard Input in the following format:
X t

-----Output-----
Print the number of sand in the upper bulb after t second.

-----Sample Input-----
100 17

-----Sample Output-----
83

17 out of the initial 100 grams of sand will be consumed, resulting in 83 grams.
"""

def calculate_remaining_sand(X: int, t: int) -> int:
    """
    Calculate the amount of sand remaining in the upper bulb after t seconds.

    Parameters:
    - X (int): The initial amount of sand in the upper bulb.
    - t (int): The number of seconds that have passed.

    Returns:
    - int: The amount of sand remaining in the upper bulb after t seconds.
    """
    return max(X - t, 0)