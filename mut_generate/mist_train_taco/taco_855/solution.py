"""
QUESTION:
Takahashi's house has only one socket.
Takahashi wants to extend it with some number of power strips, each with A sockets, into B or more empty sockets.
One power strip with A sockets can extend one empty socket into A empty sockets.
Find the minimum number of power strips required.

-----Constraints-----
 - All values in input are integers.
 - 2 \leq A \leq 20
 - 1 \leq B \leq 20

-----Input-----
Input is given from Standard Input in the following format:
A B

-----Output-----
Print the minimum number of power strips required.

-----Sample Input-----
4 10

-----Sample Output-----
3

3 power strips, each with 4 sockets, extend the socket into 10 empty sockets.
"""

import math

def calculate_minimum_power_strips(A: int, B: int) -> int:
    """
    Calculate the minimum number of power strips required to extend the socket 
    into B or more empty sockets, given each power strip has A sockets.

    Parameters:
    - A (int): Number of sockets in each power strip.
    - B (int): Desired number of empty sockets.

    Returns:
    - int: Minimum number of power strips required.
    """
    return math.ceil((B - 1) / (A - 1))