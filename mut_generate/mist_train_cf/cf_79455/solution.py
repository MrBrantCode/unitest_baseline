"""
QUESTION:
Create a function `kidsWithCandies(candies, extraCandies)` that determines which children have the potential to have the most candies. The function takes an array `candies` representing the number of candies each child has and an integer `extraCandies` representing the number of extra candies that can be given to a child. The function should return a boolean array where the ith element is true if the ith child can have the most candies and false otherwise.

Restrictions: 2 ≤ candies.length ≤ 100, 1 ≤ candies[i] ≤ 100, 1 ≤ extraCandies ≤ 50.
"""

def kidsWithCandies(candies, extraCandies):
    maxCandy = max(candies)
    return [candy+extraCandies >= maxCandy for candy in candies]