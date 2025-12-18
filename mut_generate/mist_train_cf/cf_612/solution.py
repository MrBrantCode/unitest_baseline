"""
QUESTION:
Write a function called `reverse_array` that takes an array of positive integers as input, reverses the order of the elements, and returns the reversed array in descending order without modifying the original array. The function should have a time complexity of O(n), where n is the length of the input array, and should handle cases where the input array is empty or contains duplicate elements.
"""

def reverse_array(nums):
    reversed_nums = sorted(nums[::-1], reverse=True)
    return reversed_nums