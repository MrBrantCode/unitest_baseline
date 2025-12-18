"""
QUESTION:
Write a function `common_elements` that takes two lists of integers `list1` and `list2` as input and returns a new list containing the common elements from both input lists. The function should have a time complexity of O(n^2), where n is the length of the longer input list, and a space complexity of O(1), excluding the space needed for the output list.
"""

def common_elements(list1, list2):
    common = []
    for num1 in list1:
        for num2 in list2:
            if num1 == num2 and num1 not in common:
                common.append(num1)
    return common