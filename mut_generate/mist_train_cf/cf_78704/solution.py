"""
QUESTION:
Write a Python function named `remove_duplicates` that takes one argument, a list of numbers. The function should return a new list containing all unique numbers from the input list, in the same order they appeared in the input list. If the input is not a list, the function should return the string "Error: Input should be a list." If the input list contains non-numeric elements, the function should return the string "Error: All elements in the list should be numbers."
"""

def remove_duplicates(my_list):
    # Check if input is a list
    if not isinstance(my_list, list):
        return "Error: Input should be a list."
    # Check if all elements in the list are numbers
    for element in my_list:
        if not isinstance(element, (int, float)):
            return "Error: All elements in the list should be numbers."
    # Remove duplicates and maintain order
    temp = []
    for num in my_list:
        if num not in temp:
            temp.append(num)
    return temp