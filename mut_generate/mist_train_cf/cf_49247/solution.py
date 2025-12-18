"""
QUESTION:
Create a function called `reverse_strings` that takes an array of strings as input and returns the array with its elements in reverse sequence, as well as reversing the characters in each string. If the input is not an array, return "The input is not an array". If the array is empty, return "The array is empty".
"""

def reverse_strings(arr):
    # Check if the arr is a list
    if not isinstance(arr, list):
        return "The input is not an array"
    # Check if the list is empty
    elif not arr:
        return "The array is empty"
    # Reversing the strings
    else:
        return [i[::-1] for i in arr[::-1]]