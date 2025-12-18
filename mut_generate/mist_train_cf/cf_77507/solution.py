"""
QUESTION:
Create a function `remove_duplicates` that takes an input list of integers and returns a new list with duplicates removed, preserving the original order. The function should not use any built-in Python functions or libraries. The goal is to achieve optimal memory efficiency and time complexity.
"""

def remove_duplicates(input_list):
    dict_ = {}
    result = []
    for num in input_list:
        if num not in dict_:
            dict_[num] = 1
            result.append(num)
    return result