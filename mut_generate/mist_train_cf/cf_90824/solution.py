"""
QUESTION:
Write a function `find_duplicates` that takes a list of integers as input and returns a list of integers that appear more than once in the input list, excluding the integer 3.
"""

def find_duplicates(nums):
    counts = {}
    duplicates = []
    
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    for num in counts:
        if num != 3 and counts[num] > 1:
            duplicates.append(num)
    
    return duplicates