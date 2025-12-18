"""
QUESTION:
Write a function named `sum_of_non_duplicates` that takes a list of unique integers as input and returns the sum of the non-duplicated integer elements. The function should handle negative integers, zero, and floating-point numbers, and remove all duplicate elements before calculating the sum. The input list may contain duplicate elements.
"""

def sum_of_non_duplicates(nums):
    # Remove duplicate elements using a set
    nums = list(set(nums))
    
    # Initialize the sum to zero
    total = 0
    
    # Iterate over each element in the list
    for num in nums:
        # Check if the element is not duplicated in the original list
        if nums.count(num) == 1:
            # Add the element to the sum
            total += num
    
    return total