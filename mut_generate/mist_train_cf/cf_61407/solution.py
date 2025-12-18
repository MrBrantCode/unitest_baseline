"""
QUESTION:
Implement a function `find_maximum` that takes a list of integers as input and returns the maximum integer value. If the input list is empty, the function should return `None`. The function should handle exceptions for non-integer elements in the list by ignoring them. Note that integer numbers formatted as strings (e.g., '8') are considered valid input and will be converted to integers. Float numbers will also be considered valid input, but will be compared as their integer counterpart.
"""

def find_maximum(input_list):
    if not input_list:  # Handling case of empty list
        return None
    
    max_value = None
    for i in input_list:
        try:  # Check if the element can be converted to an integer
            num = int(i)
            if max_value is None or num > max_value:
                max_value = num
        except ValueError:
            continue  # If it cannot, ignore the element
    
    return max_value