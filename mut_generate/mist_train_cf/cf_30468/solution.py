"""
QUESTION:
Vika needs to buy a minimum number of packs of candies to have at least N candies, where each pack contains M candies. Write a function `min_packs_to_buy` that takes two parameters: `N` and `M`, and returns the minimum number of packs Vika needs to buy. The function should meet the following conditions: 

- The total number of candies Vika wants, `N`, is in the range of 1 to 10^9.
- The number of candies in each pack, `M`, is in the range of 1 to 1000.
"""

def min_packs_to_buy(N: int, M: int) -> int:
    return -(-N // M) 