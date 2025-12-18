"""
QUESTION:
Write a function `find_duplicate_numbers(nums)` that takes a list of integers `nums` as input and returns a list of duplicate integers in ascending order. The input list `nums` is limited to 1000 elements and contains integers in the range of -1000 to 1000. If no duplicates are found, return "No duplicates found." The original list should not be modified.
"""

def find_duplicate_numbers(nums):
    # Create a hashmap to count occurrences
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Create a result array for duplicate numbers
    duplicates = []
    for num, freq in count.items():
        if freq > 1:
            duplicates.append(num)
    
    # Sort the result array in ascending order
    duplicates.sort()
    
    # If no duplicates found, return "No duplicates found."
    if len(duplicates) == 0:
        return "No duplicates found."
    
    return duplicates