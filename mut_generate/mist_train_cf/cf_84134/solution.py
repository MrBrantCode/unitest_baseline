"""
QUESTION:
Create a function named `shared_elements` that accepts two lists of numbers as input and returns a sorted list of unique elements that are common to both lists, excluding any group of numbers with a median that is either equal to or surpasses the highest number in each individual list. The function should have a time complexity of O(nlogn) or less, and it should not use Python's traditional list functions for sorting and duplicate removal. The input lists are non-empty and contain only numbers.
"""

import heapq

def shared_elements(list1, list2):
    # Get unique elements in each list
    set1 = set(list1)
    set2 = set(list2)

    # Get elements common to both lists
    common = list(set1 & set2)

    # Remove group of numbers with median greater than or equal to max number
    def median(lst):
        n = len(lst)
        s = sorted(lst)
        return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None

    max1 = max(list1)
    max2 = max(list2)
    common = [num for num in common if median(common) < max1 and median(common) < max2]

    # Return a new list sorted in ascending order
    return heapq.nsmallest(len(common), common)