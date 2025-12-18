"""
QUESTION:
Create a function called `get_odd_numbers` that takes a list of integers as input. The function should return a new list containing only the odd numbers from the input list, preserving their original order. If the input list is empty, the function should return the message "The input list is empty."
"""

def get_odd_numbers(input_list):
    if not input_list:
        return "The input list is empty."
    return [num for num in input_list if num % 2 != 0]