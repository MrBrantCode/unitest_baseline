"""
QUESTION:
You have N coins each of which has a value ai. Find the number of combinations that result when you choose K different coins in such a way that the total value of the coins is greater than or equal to L and less than or equal to R.

Constraints

* 1 ≤ K ≤ N ≤ 40
* 1 ≤ ai ≤ 1016
* 1 ≤ L ≤ R ≤ 1016
* All input values are given in integers

Input

The input is given in the following format.


N K L R
a1 a2 ... aN


Output

Print the number of combinations in a line.

Examples

Input

2 2 1 9
5 1


Output

1


Input

5 2 7 19
3 5 4 2 2


Output

5
"""

from bisect import bisect_left, bisect_right
from itertools import combinations

def count_valid_coin_combinations(N, K, L, R, coins):
    N_half = N // 2
    
    # Generate all possible sums of combinations for the first half of coins
    c1 = [list(map(sum, combinations(coins[:N_half], i))) for i in range(0, N_half + 1)]
    
    # Generate all possible sums of combinations for the second half of coins
    c2 = [list(map(sum, combinations(coins[N_half:], i))) for i in range(0, N - N_half + 1)]
    
    # Sort the sums of combinations for the second half
    for i in range(0, N - N_half + 1):
        c2[i].sort()
    
    ans = 0
    
    # Iterate over all possible combinations of the first half
    for i in range(0, K + 1):
        if K - i < 0 or K - i > N - N_half or i > N_half:
            continue
        
        # For each sum in the first half, find the corresponding sums in the second half
        for a in c1[i]:
            low = bisect_left(c2[K - i], L - a)
            high = bisect_right(c2[K - i], R - a)
            ans += high - low
    
    return ans