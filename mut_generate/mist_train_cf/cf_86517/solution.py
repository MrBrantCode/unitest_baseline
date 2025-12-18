"""
QUESTION:
Create a function `reverse_array` that takes an array of positive integers as input, returns a new array with the elements in reverse order, and sorts the reversed array in descending order without modifying the original array. The function should handle cases where the input array is empty or contains duplicate elements, and it should have a time complexity of O(n), where n is the length of the input array.
"""

def reverse_array(nums):
    reversed_nums = nums[::-1]  # Reverse the array
    reversed_nums.sort(reverse=True)  # Sort in descending order
    return reversed_nums