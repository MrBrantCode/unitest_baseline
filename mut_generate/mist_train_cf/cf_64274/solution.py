"""
QUESTION:
Create a function named `find_target` that takes a sorted list of numbers and a target number as input. The function should return the indices of the first and last occurrences of the target number in the list. If the target number is not found, the function should return a message indicating that the target is not in the list.
"""

def find_target(lst, target):
    try:
        first_occurrence = lst.index(target)
        last_occurrence = len(lst) - 1 - lst[::-1].index(target)
    except ValueError:
        return ("Target not found in list")
    return first_occurrence, last_occurrence