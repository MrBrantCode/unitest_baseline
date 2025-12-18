"""
QUESTION:
Create a function called `reverse_and_lower` that takes an array of strings as input, reverses the order of the elements in the array, and converts each string to lowercase. The function should return the modified array.
"""

def reverse_and_lower(arr):
    return [string.lower() for string in arr[::-1]]