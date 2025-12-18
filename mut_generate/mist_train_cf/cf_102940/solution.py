"""
QUESTION:
Find the most occurring element in an array of integers using a function named `find_majority_element`. The function should have a time complexity of O(n) and should not use any additional data structures such as dictionaries or hash maps.
"""

def find_majority_element(nums):
    """
    Find the most occurring element in an array of integers.
    
    This function uses the Boyer-Moore Voting Algorithm, which allows finding the majority element in an array without using any additional data structures.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        int: The most occurring element in the list.
    """
    candidate = None
    count = 0
    
    # First pass: Find the candidate for majority element
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1
    
    # Second pass: Confirm that the candidate is the majority element
    majority_count = sum(1 for num in nums if num == candidate)
    
    return candidate if majority_count > len(nums) / 2 else None