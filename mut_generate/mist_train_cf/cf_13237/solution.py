"""
QUESTION:
Create a function called `scale_and_sort` that takes two parameters: a list of numbers with at least 3 elements, and a multiplier. The function should return a new list where each element of the original list is multiplied by the given multiplier and the resulting list is sorted in descending order.
"""

def scale_and_sort(numbers, multiplier):
    return sorted([num * multiplier for num in numbers], reverse=True)