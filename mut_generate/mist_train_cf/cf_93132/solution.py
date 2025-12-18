"""
QUESTION:
Create a function `create_sorted_even_array` that takes an input array of integers with at least 10 elements and returns a new array containing only the even numbers from the input array, sorted in ascending order.
"""

def create_sorted_even_array(arr):
    return sorted([num for num in arr if num % 2 == 0])