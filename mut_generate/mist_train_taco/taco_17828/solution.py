"""
QUESTION:
In this Kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value. 


More examples in test cases. 

Good luck!

Please also try [Simple time difference](https://www.codewars.com/kata/5b76a34ff71e5de9db0000f2)
"""

from collections import Counter

def sort_by_frequency_and_value(arr):
    """
    Sorts elements in the array by decreasing frequency of elements.
    If two elements have the same frequency, sorts them by increasing value.

    Parameters:
    arr (list): A list of elements to be sorted.

    Returns:
    list: A sorted list of elements based on the specified criteria.
    """
    frequency_count = Counter(arr)
    return sorted(arr, key=lambda k: (-frequency_count[k], k))