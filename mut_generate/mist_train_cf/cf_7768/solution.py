"""
QUESTION:
Write a function `remove_duplicates(my_list)` that takes a list of elements as input and returns a new list containing the unique elements from `my_list` in the same order as they appeared in the original list. The function should have a time complexity of O(n^2) and use O(n) additional space. The function should not use any built-in functions or data structures beyond basic lists and control structures.
"""

def remove_duplicates(my_list):
    unique_list = []
    for num in my_list:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list