"""
QUESTION:
Write a function `calculate_total` that calculates the total of the numbers in an array that are greater than 10 and less than 20. If there are no numbers in the array that satisfy this condition, return -1.
"""

def calculate_total(arr):
    total = sum(num for num in arr if 10 < num < 20)
    return total if total > 0 else -1