"""
QUESTION:
Given a list of N lists of M integers, determine if it's possible to sort the main list and all individual lists in non-decreasing order by reversing any sublist any number of times and removing one element from each individual list. If the main list or any individual list is empty, return True. Return True if all lists can be sorted with these operations, False otherwise.
"""

def can_be_sorted(data):
    def check_sort(l):
        for i in range(len(l)):
            l_new = l[:i] + l[i+1:]
            if l_new == sorted(l_new) or l_new == sorted(l_new, reverse=True):
                return True
        return False

    for l in data:
        if not check_sort(l):
            return False
    return True