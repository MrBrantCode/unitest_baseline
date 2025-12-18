"""
QUESTION:
Create a recursive function named `binary_search` that performs a binary search on two sorted lists of integers (one list containing negative integers and the other list containing non-negative integers). The function should take a sorted list, a target value, and the lower and upper bounds of the list as parameters. It should return the index of the target value if found, or -1 if not found. Use this function in another function named `find_common_elements` that takes two sorted lists as parameters and returns a list of common elements between the two lists. The lists should not contain any duplicate values.
"""

def binary_search(list, low, high, x):
    if high >= low :
        mid = (high + low) // 2
        if list[mid] == x :
            return mid
        elif list[mid] > x :
            return binary_search(list, low, mid - 1, x)
        else :
            return binary_search(list, mid + 1, high, x)
    else :
        return -1