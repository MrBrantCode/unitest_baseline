"""
QUESTION:
Given an unsorted list of integers, write a function named `find_sole_entities` that generates a new array of unique integers (values that only appear once in the given array) in descending order. The function should take a list of integers as input and return a list of integers.
"""

def find_sole_entities(nums):
    freq = dict()
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    sole_entities = [num for num, count in freq.items() if count == 1]
    sole_entities.sort(reverse=True)
    return sole_entities