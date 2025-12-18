"""
QUESTION:
Write a function `sum_non_duplicates` that takes a list of unique integers as input and returns the sum of the non-duplicated integer elements. The function should handle negative integers, zero, and floating-point numbers, and it should only use a constant amount of additional memory, without using any additional data structures such as sets or dictionaries.
"""

def sum_non_duplicates(nums):
    # Remove duplicates by iterating over the list and keeping only the first occurrence of each element
    for i in range(len(nums)):
        if nums[i] is not None:
            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    nums[j] = None
    
    # Calculate the sum of the non-duplicated elements
    total = 0
    for num in nums:
        if num is not None:
            total += num
    
    return total