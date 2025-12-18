"""
QUESTION:
Implement a function named `remove_element` that takes two parameters: a list of elements and a target element. The function should return a new list with all occurrences of the target element removed, maintaining the original order of the remaining elements. If the target element is not present in the list, the function should return the original list unchanged. The time complexity should be O(n) and the space complexity should be O(n), where n is the size of the list.
"""

def remove_element(lst, target):
    result = []
    for element in lst:
        if element != target:
            result.append(element)
    return result