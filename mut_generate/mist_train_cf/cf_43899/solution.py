"""
QUESTION:
Write a function `reverse_last_three` that takes a list as input and returns a new list with the last three items in reverse order. If the list has fewer than three items, return the original list.
"""

def reverse_last_three(my_list):
    return my_list[:-3] + my_list[-3:][::-1]