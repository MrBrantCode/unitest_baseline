"""
QUESTION:
Create a function named `common_elements` that takes two lists of integers as input and returns a new list containing only the common elements between the two input lists. The function should have a time complexity of O(n^2), where n is the length of the longer input list.
"""

def common_elements(list1, list2):
    common = []
    for num1 in list1:
        for num2 in list2:
            if num1 == num2 and num1 not in common:
                common.append(num1)
    return common