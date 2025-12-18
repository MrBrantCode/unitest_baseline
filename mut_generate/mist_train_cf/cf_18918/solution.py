"""
QUESTION:
Create a function named `find_common_elements` that takes two lists of integers as input. The function should return a new list containing the elements that are present in both input lists, are divisible by 3, and not divisible by 5. The function must remove any duplicate elements from the result.
"""

def find_common_elements(list1, list2):
    common_elements = []
    for num in list1:
        if num % 3 == 0 and num % 5 != 0:
            if num in list2 and num not in common_elements:
                common_elements.append(num)
    return common_elements