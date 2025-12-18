"""
QUESTION:
Write a function named `find_fulcrum` that takes a list of integers as input and returns the index of the "fulcrum" element. The fulcrum element is the element where the sum of all numbers before it equals the average of all numbers after it. If no such element exists, the function should return -1. The function should only consider elements at indices 1 through the second-to-last index.
"""

def find_fulcrum(lst):
    for i in range(1, len(lst)-1):   # Do not consider the first and last element
        if sum(lst[:i]) == sum(lst[i+1:])/len(lst[i+1:]):
            return i
    return -1   # Return -1 if there is no fulcrum