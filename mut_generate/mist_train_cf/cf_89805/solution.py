"""
QUESTION:
Write a function called `find_common_elements` that takes two arrays of integers as input and returns a list of integers that are common to both arrays. You can use loops but cannot use any built-in functions or libraries. The function should be able to handle arrays of any length.
"""

def find_common_elements(arr1, arr2):
    common_elements = []
    
    for num1 in arr1:
        for num2 in arr2:
            if num1 == num2 and num1 not in common_elements:
                common_elements.append(num1)
    
    return common_elements