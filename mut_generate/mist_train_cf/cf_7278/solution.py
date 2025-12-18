"""
QUESTION:
Implement a function called "first_duplicate" that takes an array of integers as input and returns the first duplicate element found in the array. If no duplicate is found, the function should return -1. The function must have a time complexity of O(n) and a space complexity of O(1), where n is the length of the array. It should be implemented using a single loop and without using any additional data structures to store visited elements, and it should minimize the number of comparisons made.
"""

def first_duplicate(nums):
    """
    This function finds and returns the first duplicate element in an array of integers.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        int: The first duplicate element found in the array. If no duplicate is found, returns -1.
    """
    # We start by iterating over the array
    for i in range(len(nums)):
        # For each element, we check if its absolute value is less than or equal to the length of the array
        # This is to ensure that the index is within the bounds of the array
        if abs(nums[i]) <= len(nums):
            # If the element at the index of the current element's absolute value is negative, 
            # it means we've seen this element before, so we return it
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            # If not, we mark the element at the index of the current element's absolute value as negative
            else:
                nums[abs(nums[i]) - 1] *= -1
    # If we've iterated over the entire array and haven't found any duplicates, we return -1
    return -1