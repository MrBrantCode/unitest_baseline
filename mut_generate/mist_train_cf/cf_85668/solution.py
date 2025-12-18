"""
QUESTION:
Construct a function `handle_input(input_str)` that takes a string as input and handles the string "Felis catus" while considering the following cases: null input, empty string, non-string input, numeric input, and case sensitivity. The function should return a corresponding message for each case.
"""

def handle_input(input_str):
    if input_str is None:
        return "Input is Null"
    elif isinstance(input_str, str) is False:
        return "Input is not a String"
    elif input_str == "":
        return "Input is Empty"
    elif input_str.isdigit():
        return "Input is Numeric"
    
    lowered_input = input_str.lower()
    
    if lowered_input == "felis catus":
        return "Input is Felis catus"
    else:
        return "Input is unrecognized"