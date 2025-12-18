"""
QUESTION:
There is a kangaroo at coordinate 0 on an infinite number line that runs from left to right, at time 0.
During the period between time i-1 and time i, the kangaroo can either stay at his position, or perform a jump of length exactly i to the left or to the right.
That is, if his coordinate at time i-1 is x, he can be at coordinate x-i, x or x+i at time i.
The kangaroo's nest is at coordinate X, and he wants to travel to coordinate X as fast as possible.
Find the earliest possible time to reach coordinate X.

-----Constraints-----
 - X is an integer.
 - 1≤X≤10^9

-----Input-----
The input is given from Standard Input in the following format:
X

-----Output-----
Print the earliest possible time for the kangaroo to reach coordinate X.

-----Sample Input-----
6

-----Sample Output-----
3

The kangaroo can reach his nest at time 3 by jumping to the right three times, which is the earliest possible time.
"""

def earliest_time_to_reach(X: int) -> int:
    """
    Calculate the earliest possible time for a kangaroo to reach coordinate X on an infinite number line.

    The kangaroo starts at coordinate 0 at time 0 and can either stay at his position or perform a jump of length exactly i to the left or to the right during the period between time i-1 and time i.

    Parameters:
    X (int): The target coordinate to reach.

    Returns:
    int: The earliest possible time to reach coordinate X.
    """
    ans = 0
    a = 0
    for i in range(1, X + 1):
        a += i
        ans += 1
        if a >= X:
            return ans