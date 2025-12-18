"""
QUESTION:
Create a function `solve(arr)` that takes an array of numbers `arr` as input and returns a tuple containing two values. The first value is the sum of the numbers and their corresponding indices in the array that are divisible by 3, and the second value is the arithmetic mean of these filtered numbers. If no numbers are divisible by 3, the mean should be 0.
"""

def solve(arr):
    filtered = [(i, n) for i, n in enumerate(arr) if n % 3 == 0]
    sum_filtered = sum(i + n for i, n in filtered)
    mean_filtered = sum(n for _, n in filtered) / len(filtered) if filtered else 0
    return sum_filtered, mean_filtered