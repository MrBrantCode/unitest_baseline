"""
QUESTION:
Sort the array of odd numbers, including negative numbers, in descending order by their absolute values using a function named `sort_odds(arr)`. The function should take one argument `arr` as an array of integers.
"""

def sort_odds(arr):
    return sorted(arr, key=abs, reverse=True)