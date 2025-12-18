"""
QUESTION:
Write a function `get_non_unique_elements(lst)` that generates a list containing only the non-unique elements from the input list `lst`. The function should not use any built-in functions or libraries and should have a time complexity of O(n^2). The function should return a list where each non-unique element appears only once.
"""

def get_non_unique_elements(lst):
    non_unique_elements = []
    for i in range(len(lst)):
        count = 0
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                count += 1
        if count > 0 and lst[i] not in non_unique_elements:
            non_unique_elements.append(lst[i])
    return non_unique_elements