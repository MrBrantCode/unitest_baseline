"""
QUESTION:
Write a function `is_palindrome(lst)` that checks if a given list of up to 100 elements is a palindrome, ignoring non-numeric elements and considering negative and decimal numbers. The function should have a time complexity of O(n), where n is the length of the list.
"""

def is_palindrome(lst):
    # Create a filtered list of numeric elements only
    nums = [x for x in lst if isinstance(x, (int, float))]

    # Check if the filtered list is a palindrome
    return nums == nums[::-1]