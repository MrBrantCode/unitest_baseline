"""
QUESTION:
Find the maximum pair of elements from two lists such that no element is repeated. 

Write a function named `find_max_pair` that takes two lists of numbers as input. Return a tuple of two numbers, one from each list, that have the maximum combined value. If the maximum elements in both lists are the same, return the maximum element from one list and the second-largest element from the other list.
"""

def find_max_pair(list1, list2):
    if max(list1) != max(list2):
        return (max(list1), max(list2))
    else:
        if sorted(list1)[-2] > sorted(list2)[-2]:
            return (sorted(list1)[-2], max(list2))
        else:
            return (max(list1), sorted(list2)[-2])