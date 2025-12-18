"""
QUESTION:
Design a function `remove_duplicates(nums)` that removes all duplicate integers from an unsorted array `nums` in-place and returns the updated length of the array. The function should have a time complexity of O(n), where n is the number of elements in the array.
"""

def remove_duplicates(nums):
    # Create an empty hash set
    unique_nums = set()
    
    # Index to keep track of the last non-duplicate element
    last_non_duplicate = 0
    
    # Iterate over the array
    for i in range(len(nums)):
        # Check if the current element is unique
        if nums[i] not in unique_nums:
            # Add the current element to the hash set
            unique_nums.add(nums[i])
            
            # Swap the current element with the last non-duplicate element
            nums[last_non_duplicate] = nums[i]
            
            # Update the index of the last non-duplicate element
            last_non_duplicate += 1
    
    # Remove the remaining elements after the last non-duplicate element
    del nums[last_non_duplicate:]
    
    # Return the updated length of the array
    return last_non_duplicate