"""
QUESTION:
Write a function `find_smallest_positive_integer(lst)` that takes a list of integers as input and returns the smallest positive integer that is not present in the list. The input list can contain up to 1,000,000 integers, including positive and negative integers, and may contain duplicates. The function should have a space complexity of O(1) or O(n) if not achievable, and should not use any additional data structures or libraries.
"""

def find_smallest_positive_integer(lst):
    # Remove duplicates and sort the list in ascending order
    lst = sorted(set(lst))
    
    # Check if the list is empty or if the first element is greater than 1
    if not lst or lst[0] > 1:
        return 1
    
    # Iterate through the sorted list and find the first gap between consecutive elements
    for i in range(len(lst) - 1):
        if lst[i+1] - lst[i] > 1:
            return lst[i] + 1
    
    # If there are no gaps, return the next positive integer after the last element
    return lst[-1] + 1