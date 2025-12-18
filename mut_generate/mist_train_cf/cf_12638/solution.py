"""
QUESTION:
Write a function named `find_highest_value` that takes a list of integers as input and returns the highest value in the list without using any built-in functions or methods that directly sort or find the maximum value. The function should handle cases where the list may contain duplicate values or negative numbers.
"""

def find_highest_value(my_list):
    highest_value = float("-inf")
    for num in my_list:
        if num > highest_value:
            highest_value = num
    return highest_value