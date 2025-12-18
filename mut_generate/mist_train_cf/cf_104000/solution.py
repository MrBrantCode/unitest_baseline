"""
QUESTION:
Given a list of unique integers, write a function `sum_non_duplicated_elements` that returns the sum of the non-duplicated integer elements. The function should handle negative integers and zero.
"""

def sum_non_duplicated_elements(nums):
    # Create an empty set to store the duplicated elements
    duplicates = set()
    # Create a variable to store the sum of non-duplicated elements
    sum_non_duplicates = 0
    
    # Iterate through each element in the list
    for num in nums:
        # Check if the element is already in the duplicates set
        if num in duplicates:
            # If it is, continue to the next iteration
            continue
        # Check if the element is already in the nums list
        elif nums.count(num) > 1:
            # If it is, add it to the duplicates set
            duplicates.add(num)
        # If the element is unique, add it to the sum_non_duplicates variable
        sum_non_duplicates += num
    
    return sum_non_duplicates