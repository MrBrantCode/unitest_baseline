"""
QUESTION:
Implement a function `process_input(input)` that processes a given input and returns a specific output based on the input type. The function should follow these rules: 
- If the input is an integer, return the input multiplied by 2.
- If the input is a string, return the input concatenated with " World".
- If the input is a list, return the input with all elements doubled.
- If the input is a dictionary, return the input with all values multiplied by 2.
- If the input is of any other type, return "Returning Hello".
"""

def entrance(input):
    if isinstance(input, int):
        return input * 2
    elif isinstance(input, str):
        return input + " World"
    elif isinstance(input, list):
        return [x * 2 for x in input]
    elif isinstance(input, dict):
        return {key: value * 2 for key, value in input.items()}
    else:
        return "Returning Hello"