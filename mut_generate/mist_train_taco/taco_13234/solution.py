"""
QUESTION:
We have an integer N.
Print an integer x between N and 10^{13} (inclusive) such that, for every integer y between 2 and N (inclusive), the remainder when x is divided by y is 1.
Under the constraints of this problem, there is always at least one such integer x.

-----Constraints-----
 - All values in input are integers.
 - 2 \leq N \leq 30

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print an integer x between N and 10^{13} (inclusive) such that, for every integer y between 2 and N (inclusive), the remainder when x is divided by y is 1.
If there are multiple such integers, any of them will be accepted.

-----Sample Input-----
3

-----Sample Output-----
7

The remainder when 7 is divided by 2 is 1, and the remainder when 7 is divided by 3 is 1, too.
7 is an integer between 3 and 10^{13}, so this is a desirable output.
"""

import math
from functools import reduce

def find_special_integer(N: int) -> int:
    """
    Finds an integer x between N and 10^13 (inclusive) such that for every integer y between 2 and N (inclusive),
    the remainder when x is divided by y is 1.

    Parameters:
    N (int): The input integer.

    Returns:
    int: The special integer x.
    """
    
    def lcm_base(x, y):
        return x * y // math.gcd(x, y)

    def lcm(*numbers):
        return reduce(lcm_base, numbers, 1)
    
    A = [i for i in range(2, N + 1)]
    X = lcm(*A) + 1
    
    return X