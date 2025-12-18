"""
QUESTION:
Write a function `find_common_elements` that takes two arrays of integers, `arr1` and `arr2`, as input and returns a list of their common elements without using any built-in functions or libraries, such as set() or intersection().
"""

def find_common_elements(arr1, arr2):
    common_elements = []
    for num1 in arr1:
        for num2 in arr2:
            if num1 == num2 and num1 not in common_elements:
                common_elements.append(num1)
    return common_elements