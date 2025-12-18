"""
QUESTION:
Write a function called `find_common_elements` that takes two lists of numbers as input and returns a new list containing the common elements from both lists, considering duplicate elements separately.
"""

def find_common_elements(list1, list2):
    common_elements = []
    for num in list1:
        if num in list2:
            common_elements.append(num)
            list2.remove(num)
    return common_elements