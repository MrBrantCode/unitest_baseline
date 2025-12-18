"""
QUESTION:
Create a function named `test_divisibility` that takes two integers `a` and `b` as input, checks if they are positive, and returns `True` if `a` is evenly divisible by `b`, and an error message otherwise.

Additionally, create another function named `find_divisible_pairs` that takes an array of integers as input, uses the `test_divisibility` function to find all pairs of evenly divisible numbers in the array, and returns these pairs. The function should ignore pairings where a number is divided by itself and should be able to handle large arrays efficiently.
"""

def test_divisibility(a, b):
    if a <= 0 or b <= 0:
        return "Error: Both numbers should be positive."
    
    return a % b == 0


def find_divisible_pairs(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if test_divisibility(arr[i], arr[j]):
                pairs.append((arr[i], arr[j]))
            elif test_divisibility(arr[j], arr[i]):
                pairs.append((arr[j], arr[i]))
    return pairs