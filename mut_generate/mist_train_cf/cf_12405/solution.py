"""
QUESTION:
Write a function `find_duplicates` that takes in a list of integers `nums` and returns a list of all duplicate numbers in `nums` in the order they appear. The function should have a time complexity of O(n) and space complexity of O(n), without using any built-in functions or libraries.
"""

def find_duplicates(nums):
    """
    This function finds all duplicate numbers in a given list and returns them in the order they appear.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: A list of duplicate numbers in the order they appear.
    """
    seen = set()
    duplicates = set()
    result = []
    
    for num in nums:
        if num in seen:
            if num not in duplicates:
                result.append(num)
            duplicates.add(num)
        else:
            seen.add(num)
            
    return result