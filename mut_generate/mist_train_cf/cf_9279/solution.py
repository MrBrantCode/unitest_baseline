"""
QUESTION:
Create a function called `find_duplicates` that takes an array of integers as input and returns an array of integers that appear more than once in the input array, excluding the integer 3.
"""

def find_duplicates(nums):
    counts = {}
    
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    return [num for num in counts if num != 3 and counts[num] > 1]