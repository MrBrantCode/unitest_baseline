"""
QUESTION:
We have N integers. The i-th number is A_i.
\{A_i\} is said to be pairwise coprime when GCD(A_i,A_j)=1 holds for every pair (i, j) such that 1\leq i < j \leq N.
\{A_i\} is said to be setwise coprime when \{A_i\} is not pairwise coprime but GCD(A_1,\ldots,A_N)=1.
Determine if \{A_i\} is pairwise coprime, setwise coprime, or neither.
Here, GCD(\ldots) denotes greatest common divisor.

-----Constraints-----
 - 2 \leq N \leq 10^6
 - 1 \leq A_i\leq 10^6

-----Input-----
Input is given from Standard Input in the following format:
N
A_1 \ldots A_N

-----Output-----
If \{A_i\} is pairwise coprime, print pairwise coprime; if \{A_i\} is setwise coprime, print setwise coprime; if neither, print not coprime.

-----Sample Input-----
3
3 4 5

-----Sample Output-----
pairwise coprime

GCD(3,4)=GCD(3,5)=GCD(4,5)=1, so they are pairwise coprime.
"""

from math import gcd
from typing import List

def determine_coprimeness(A: List[int]) -> str:
    """
    Determines if the list of integers A is pairwise coprime, setwise coprime, or neither.

    Parameters:
    A (List[int]): A list of integers.

    Returns:
    str: A string indicating whether the list is "pairwise coprime", "setwise coprime", or "not coprime".
    """
    n = len(A)
    m = max(A)
    c = [0] * (m + 1)
    g = A[0]
    
    for i in A:
        g = gcd(g, i)
        c[i] = 1
    
    if g > 1:
        return "not coprime"
    
    for i in range(2, 10 ** 6 + 1):
        if sum(c[i::i]) > 1:
            return "setwise coprime"
    
    return "pairwise coprime"