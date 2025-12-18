"""
QUESTION:
Alex and Lee continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 
Alex and Lee take turns, with Alex starting first.  Initially, M = 1.
On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
The game continues until all the stones have been taken.
Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.
 
Example 1:
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

 
Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 10 ^ 4
"""

from functools import lru_cache
from math import inf

def max_alex_stones(piles):
    """
    Calculate the maximum number of stones Alex can get assuming both players play optimally.

    Parameters:
    piles (List[int]): A list of integers where each integer represents the number of stones in a pile.

    Returns:
    int: The maximum number of stones Alex can get.
    """
    a = []
    s = 0
    n = len(piles)
    for i in piles[::-1]:
        s += i
        a.append(s)
    a = a[::-1]

    @lru_cache(None)
    def fun(i, m):
        if i + 2 * m >= n:
            return a[i]
        mn = inf
        for ii in range(1, 2 * m + 1):
            if ii > m:
                ans = fun(i + ii, ii)
            else:
                ans = fun(i + ii, m)
            if ans < mn:
                mn = ans
        return a[i] - mn
    
    return fun(0, 1)