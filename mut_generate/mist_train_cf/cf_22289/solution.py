"""
QUESTION:
Implement a function `remove_duplicates` that takes a list of integers as input and returns a list containing the unique elements from the input list in the same order as they appeared in the original list. The function should have a time complexity of O(n) and use O(n) additional space. The function should not use any built-in functions or data structures.
"""

def remove_duplicates(my_list):
    seen = set()
    result = []
    for num in my_list:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result