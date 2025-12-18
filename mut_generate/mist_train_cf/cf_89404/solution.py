"""
QUESTION:
Write a function called `find_elements` that takes an array of integers as input and returns the maximum, minimum, second maximum, and second minimum elements in a single pass with a time complexity of O(n). The array can contain both positive and negative integers, may have duplicate elements, and will not exceed 1000 elements. If the array is empty, return None for all required elements. Do not use built-in functions or sorting algorithms to find these elements.
"""

def find_elements(arr):
    if len(arr) == 0:
        return None, None, None, None

    max_element = float('-inf')
    min_element = float('inf')
    second_max_element = float('-inf')
    second_min_element = float('inf')

    for num in arr:
        if num > max_element:
            second_max_element = max_element
            max_element = num
        elif num > second_max_element and num != max_element:
            second_max_element = num

        if num < min_element:
            second_min_element = min_element
            min_element = num
        elif num < second_min_element and num != min_element:
            second_min_element = num

    return max_element, min_element, second_max_element, second_min_element