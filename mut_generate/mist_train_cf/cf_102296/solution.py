"""
QUESTION:
Create a function `find_max_element` that takes a list of elements as input and returns the maximum element. The list may contain both positive and negative integers, as well as non-integer elements. The function must have a time complexity of O(n) and cannot use built-in functions or methods that directly provide the maximum element in a list, or additional data structures to store intermediate results.
"""

def find_max_element(lst):
    max_element = lst[0]
    for i in range(1, len(lst)):
        if isinstance(lst[i], (int, float)) and lst[i] > max_element:
            max_element = lst[i]
    return max_element