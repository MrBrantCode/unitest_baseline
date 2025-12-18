"""
QUESTION:
Implement the `intricate_sort` function. The function takes a list of lists of integers as input and returns a boolean value. The function should return True if it's possible to sort the main list and all individual lists in a non-decreasing sequence by reversing any sublist's sequence and/or subtracting one element from each single list, and False otherwise. If the input list or any individual list is empty, the function should return True. The input list and individual lists may contain duplicate elements.
"""

def intricate_sort(details):
    for group in details:
        sorted_group = sorted(group)
        reversed_group = sorted(group, reverse=True)
        
        if group != sorted_group and group != reversed_group:
            if len(group) > 1:
                group.remove(min(group))
            else:
                return False

            if group != sorted(group) and group != sorted(group, reverse=True):
                return False

    return sorted([item for sublist in details for item in sublist]) == [item for sublist in details for item in sublist]