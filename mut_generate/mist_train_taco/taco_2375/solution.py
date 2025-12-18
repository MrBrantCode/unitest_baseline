"""
QUESTION:
You want to make change for $ n $ cents. Assuming that you have infinite supply of coins of 1, 5, 10 and / or 25 cents coins respectively, find the minimum number of coins you need.

Constraints

* $ 1 \ le n \ le 10 ^ 9 $

Input


$ n $


The integer $ n $ is given in a line.

output

Print the minimum number of coins you need in a line.

Examples

Input

100


Output

4


Input

54321


Output

2175
"""

def minimum_coins(n: int) -> int:
    COIN = [25, 10, 5, 1]
    ans = 0
    for coin in COIN:
        ans += n // coin
        n %= coin
    return ans