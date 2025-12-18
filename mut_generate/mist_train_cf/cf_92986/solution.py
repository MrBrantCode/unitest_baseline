"""
QUESTION:
Create a function `filter_and_sort_range` that takes a range as input and returns a list of odd numbers from the range, sorted in descending order. The function should not include any even numbers in the output.
"""

def filter_and_sort_range(r):
    return sorted([num for num in r if num % 2 != 0], reverse=True)