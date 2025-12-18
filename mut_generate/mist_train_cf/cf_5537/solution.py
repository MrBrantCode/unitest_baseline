"""
QUESTION:
Create a function `find_max` that returns the maximum element of a given list. The input list contains at least two elements, the maximum element is unique, and the function should only iterate through the list once. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input list.
"""

def find_max(lst):
    max_element = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_element:
            max_element = lst[i]
    return max_element