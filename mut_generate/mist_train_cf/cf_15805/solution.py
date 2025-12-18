"""
QUESTION:
Create a function `sort_and_join` that takes a list of integers as input, sorts the numbers in ascending order, and returns them as a comma-separated string. The time complexity of the solution must be less than O(nlogn).
"""

def sort_and_join(numbers):
    return ",".join(str(number) for number in sorted(numbers))