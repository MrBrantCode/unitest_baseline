"""
QUESTION:
Create a function called `findUniqueDuplicates` that takes a list of integers as input and returns a list of integers that occur more than once in the input list. The function should not modify the original list. The input list can be empty, contain negative numbers, and have duplicate elements in any order. The function should return a list of unique integers that occur more than once in the input list.
"""

def findUniqueDuplicates(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    unique_duplicates = [num for num, c in count.items() if c > 1]
    return unique_duplicates