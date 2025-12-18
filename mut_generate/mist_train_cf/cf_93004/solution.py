"""
QUESTION:
Write a Python function named `find_common_elements` that takes two arrays of integers, `arr1` and `arr2`, as input and returns a list of integers that are common to both arrays. The function must not use any built-in functions or libraries, such as set() or intersection(), to find the common elements.
"""

def find_common_elements(arr1, arr2):
    common_elements = []
    for num1 in arr1:
        for num2 in arr2:
            if num1 == num2 and num1 not in common_elements:
                common_elements.append(num1)
    return common_elements