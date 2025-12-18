"""
QUESTION:
You are given four integers A, B, C, and D. Find the number of integers between A and B (inclusive) that can be evenly divided by neither C nor D.

-----Constraints-----
 - 1\leq A\leq B\leq 10^{18}
 - 1\leq C,D\leq 10^9
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
A B C D

-----Output-----
Print the number of integers between A and B (inclusive) that can be evenly divided by neither C nor D.

-----Sample Input-----
4 9 2 3

-----Sample Output-----
2

5 and 7 satisfy the condition.
"""

import math

def count_integers_not_divisible(A: int, B: int, C: int, D: int) -> int:
    """
    Counts the number of integers between A and B (inclusive) that are not divisible by C or D.

    Parameters:
    A (int): The lower bound of the range (inclusive).
    B (int): The upper bound of the range (inclusive).
    C (int): The first divisor.
    D (int): The second divisor.

    Returns:
    int: The number of integers between A and B (inclusive) that are not divisible by C or D.
    """
    
    def lcm(x, y):
        return x * y // math.gcd(x, y)
    
    l = lcm(C, D)
    temp = l - (l // C + l // D - 1)
    a = (A - 1) % l
    b = B % l
    aa = (A - 1) // l
    bb = B // l
    tempA = a - (a // C + a // D - 1)
    tempB = b - (b // C + b // D - 1)
    ans = temp * bb + tempB - (temp * aa + tempA)
    
    return ans