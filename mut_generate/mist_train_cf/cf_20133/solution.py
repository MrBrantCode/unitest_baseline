"""
QUESTION:
Implement a function named `find_highest_value` that takes a list of integers as input and returns the highest value in the list. The function should not use any built-in sorting or max-finding methods. It must handle lists containing duplicate values, negative numbers, and empty lists, and should have a time complexity of O(n), where n is the length of the list.
"""

def find_highest_value(my_list):
    if len(my_list) == 0:
        return None
    highest_value = my_list[0]
    for num in my_list:
        if num > highest_value:
            highest_value = num
    return highest_value