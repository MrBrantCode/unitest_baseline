"""
QUESTION:
Write a Python function named `find_highest_number` that takes a list of integers as input and returns the highest number in the list. The function should return an error message if the input list is empty or contains non-integer elements. The function should be able to handle lists of any length and cases where the input list contains duplicates.
"""

def find_highest_number(my_list):
    # Check if the input list is empty
    if len(my_list) == 0:
        return "Error: The input list is empty."
    # Check if the input list contains non-integer elements
    for element in my_list:
        if type(element) != int:
            return "Error: The input list contains non-integer elements."
    # Find the highest number in the list
    highest = my_list[0]
    for num in my_list:
        if num > highest:
            highest = num
    return highest