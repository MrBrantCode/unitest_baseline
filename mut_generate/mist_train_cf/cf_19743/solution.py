"""
QUESTION:
Create a function named `get_count_and_sum` that takes a list of integers as input and checks if all elements are unique, in ascending order, and even numbers. If the conditions are met, return the total count of unique elements and the sum of all elements in the list. The function should have a time complexity of less than O(n^2).
"""

def get_count_and_sum(lst):
    # Check if all elements are unique
    if len(lst) != len(set(lst)):
        return None

    # Check if elements are in ascending order
    if lst != sorted(lst):
        return None

    # Check if all elements are even numbers
    if any(num % 2 != 0 for num in lst):
        return None

    unique_count = len(set(lst))
    total_sum = sum(lst)
    return unique_count, total_sum