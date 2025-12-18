"""
QUESTION:
Implement a function `odd_count` that takes a list of integers as input and returns a tuple containing the count of odd integers in the list and a boolean indicating whether this count is odd.
"""

def odd_count(lst):
    odd_count = 0
    for num in lst:
        if num % 2 != 0:
            odd_count += 1
    return odd_count, odd_count % 2 != 0