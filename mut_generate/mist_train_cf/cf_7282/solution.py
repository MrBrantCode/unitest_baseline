"""
QUESTION:
Create a function called `get_odd_numbers` that takes a list of numbers as input, preserves the original order, and returns a new list containing only the odd numbers. If the input list is empty, return the message "Input list is empty." The function should have a time complexity of O(n), where n is the length of the input list.
"""

def get_odd_numbers(input_list):
    if not input_list:
        return "Input list is empty."
    
    odd_numbers = []
    for num in input_list:
        if num % 2 != 0:
            odd_numbers.append(num)
    
    return odd_numbers