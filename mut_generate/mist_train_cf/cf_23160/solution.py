"""
QUESTION:
Write a function `sum_of_non_duplicates(nums)` that takes a list of unique or non-unique integers and/or floating-point numbers as input, removes all duplicate elements, and returns the sum of the remaining non-duplicated integer and floating-point number elements. The function should be able to handle negative integers, zero, and floating-point numbers.
"""

def sum_of_non_duplicates(nums):
    # Remove duplicate elements using a set
    nums = list(set(nums))
    
    # Initialize the sum to zero
    total = 0
    
    # Iterate over each element in the list
    for num in nums:
        # Check if the element is not duplicated
        if nums.count(num) == 1:
            # Add the element to the sum
            total += num
    
    return total