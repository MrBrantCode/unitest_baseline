"""
QUESTION:
Design a function `find_min_abs_difference` that takes two lists of integers as input, `list1` and `list2`, and returns the minimum absolute difference between any two elements, one from each list. The solution should have a time complexity of O(nlogn), where n is the total number of elements in both lists combined.
"""

def find_min_abs_difference(list1, list2):
    list3 = list1 + list2
    list3.sort()
    min_diff = float('inf')

    for i in range(len(list3) - 1):
        abs_diff = abs(list3[i] - list3[i+1])
        if abs_diff < min_diff:
            min_diff = abs_diff

    return min_diff