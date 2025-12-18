"""
QUESTION:
Implement a function `longest_subsequence` that takes a list of integers as input and returns the length of the longest subsequence with no repeated numbers. The subsequence can be derived from the original sequence by deleting some or no elements without changing the order of the remaining elements.
"""

def longest_subsequence(nums):
    """
    This function takes a list of integers as input and returns the length of the longest subsequence with no repeated numbers.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    int: The length of the longest subsequence with no repeated numbers.
    """
    
    # Create an empty set to store the unique elements in the current window
    unique_nums = set()
    
    # Initialize two pointers, left and right, to the start of the list
    left = 0
    max_length = 0
    
    # Iterate over the list with the right pointer
    for right in range(len(nums)):
        # While the current element is in the set, remove the leftmost element from the set and move the left pointer to the right
        while nums[right] in unique_nums:
            unique_nums.remove(nums[left])
            left += 1
        
        # Add the current element to the set
        unique_nums.add(nums[right])
        
        # Update the maximum length
        max_length = max(max_length, right - left + 1)
    
    return max_length