"""
QUESTION:
Write a function `distributeCandies(ratings)` that takes an array of integers `ratings` as input, where `ratings[i]` represents the evaluation score of the `i-th` juvenile. The function should return the minimum number of confectioneries needed to be distributed among the juveniles, following the rules that every juvenile must receive at least one confectionery and juveniles with a higher evaluation score receive more confectioneries than their adjacent counterparts.
"""

def distributeCandies(ratings):
    n = len(ratings)
    left = [1]*n
    right = [1]*n

    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            left[i] = left[i-1] + 1

    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            right[i] = right[i+1] + 1

    return sum(max(left[i], right[i]) for i in range(n))