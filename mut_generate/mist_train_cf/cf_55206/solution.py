"""
QUESTION:
You are given an array of integers `baskets` where `baskets[i]` is the number of apples in the `ith` basket. The array is of length `3n` and you need to divide the baskets into groups of three, where you pick the second most number of apples in each group. Return the maximum number of apples which you can have.

The length of the array `baskets` is between 3 and `10^5` (inclusive), and `baskets.length % 3 == 0`. Each element in the array is between 1 and `10^4` (inclusive).
"""

def entrance(baskets):
    baskets.sort(reverse=True)
    return sum(baskets[i] for i in range(0, len(baskets)//3*2, 1))