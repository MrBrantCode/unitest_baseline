"""
QUESTION:
Write a function `longest_subarray_with_distinct_elements` that takes a sequential array of whole numbers as input and returns the length of the longest continuous subarray containing the maximum number of distinct integers. The function should be efficient for large datasets.
"""

def longest_subarray_with_distinct_elements(nums):
    """
    This function takes a sequential array of whole numbers as input and returns 
    the length of the longest continuous subarray containing the maximum number 
    of distinct integers.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The length of the longest continuous subarray with distinct elements.
    """
    
    # Initialize the maximum length and the start pointer of the sliding window
    max_length = 0
    window_start = 0
    
    # Initialize a dictionary to store the frequency of each element in the current window
    char_frequency = {}
    
    # Iterate over the array with the end pointer of the sliding window
    for window_end in range(len(nums)):
        
        # Add the current element to the dictionary
        right_char = nums[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        
        # Shrink the sliding window until all elements are distinct
        while len(char_frequency) < window_end - window_start + 1:
            left_char = nums[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        
        # Update the maximum length
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length