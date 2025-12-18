"""
QUESTION:
Design a function `remove_duplicates` that takes an array as input and returns a new array containing the elements of the original array with all duplicates removed, while maintaining their original order. The function should have a time complexity of O(n) and use only a constant amount of additional space, where n is the size of the input array.
"""

def remove_duplicates(nums):
    """
    Removes duplicates from a given array while maintaining their original order.
    
    Args:
        nums (list): The input array.
    
    Returns:
        list: A new array containing the unique elements from the input array.
    """
    seen = set()
    return [num for num in nums if not (num in seen or seen.add(num))]