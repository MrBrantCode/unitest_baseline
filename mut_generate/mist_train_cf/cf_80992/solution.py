"""
QUESTION:
Create a function called `reverse_alphabetical_order` that takes an array of strings as input and returns the array sorted in reverse alphabetical order. The array contains distinct fruit names and must be sorted in a descending order (Z to A).
"""

def reverse_alphabetical_order(array):
    return sorted(array, reverse=True)