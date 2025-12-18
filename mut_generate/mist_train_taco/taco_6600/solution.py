"""
QUESTION:
In K-city, there are n streets running east-west, and m streets running north-south. Each street running east-west and each street running north-south cross each other. We will call the smallest area that is surrounded by four streets a block. How many blocks there are in K-city?

-----Constraints-----
 - 2 ≤ n, m ≤ 100

-----Input-----
Input is given from Standard Input in the following format:
n m

-----Output-----
Print the number of blocks in K-city.

-----Sample Input-----
3 4

-----Sample Output-----
6

There are six blocks, as shown below:
"""

def calculate_blocks(n: int, m: int) -> int:
    """
    Calculate the number of blocks in K-city given the number of streets running east-west and north-south.

    Parameters:
    - n (int): Number of streets running east-west.
    - m (int): Number of streets running north-south.

    Returns:
    - int: The number of blocks in K-city.
    """
    return (n - 1) * (m - 1)