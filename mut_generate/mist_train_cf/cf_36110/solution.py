"""
QUESTION:
Write a function `solution` that takes a list of binary integers (0 or 1) as input and returns the maximum number of consecutive 1's in the list.
"""

def findMaxConsecutiveOnes(nums):
    max_consecutive = 0  
    current_consecutive = 0  

    for num in nums:
        if num == 1:
            current_consecutive += 1  
            max_consecutive = max(max_consecutive, current_consecutive)  
        else:
            current_consecutive = 0  

    return max_consecutive