"""
QUESTION:
Create a function `sort_odds_evens(array)` that takes an array of numbers as input and returns a new array where odd and even numbers are sorted separately among themselves in ascending order, but their relative positions remain unchanged with respect to each other. The function should not modify the original array.
"""

def sort_odds_evens(array):
    odds = sorted([x for x in array if x % 2 == 1])
    evens = sorted([x for x in array if x % 2 == 0])
    result = []
    for x in array:
        if x % 2 == 1:
            result.append(odds.pop(0))
        else:
            result.append(evens.pop(0))
    return result