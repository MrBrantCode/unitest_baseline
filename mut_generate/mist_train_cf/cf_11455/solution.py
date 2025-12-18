"""
QUESTION:
Create a function called `retrieve_last_three` that takes an array of elements as input. The function should return a new array containing the last three elements from the input array, sorted in ascending order. If the input array has fewer than three elements, the function should return all elements in sorted order.
"""

def retrieve_last_three(array):
    return sorted(array[-3:])