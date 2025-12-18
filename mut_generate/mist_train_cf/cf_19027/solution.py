"""
QUESTION:
Create a function named `sum_odd_numbers` that takes a list of numbers as input and returns the sum of all positive odd integers in the list. The function should ignore non-integer elements and negative numbers. If the list is empty or does not contain any positive odd integers, the function should return 0.
"""

def entrance(numbers):
    total = 0

    for num in numbers:
        if isinstance(num, int) and num % 2 != 0 and num > 0:
            total += num

    return total