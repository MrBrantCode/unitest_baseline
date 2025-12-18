"""
QUESTION:
Create a function named `last_elements_reverse` that accepts an array `arr` and an integer `n` as inputs. The function should return the last `n` elements of the array in reverse order. If `n` is larger than the size of the array, return an error message indicating that the input is invalid.
"""

def last_elements_reverse(arr, n):
    if n > len(arr):
        return "Invalid input: 'n' is larger than the array size."
    else:
        return arr[-n:][::-1]