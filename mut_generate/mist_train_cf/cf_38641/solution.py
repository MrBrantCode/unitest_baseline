"""
QUESTION:
Implement the `sanitizeInput` function, which takes a string as input and returns a sanitized version of the input. The function should replace any occurrence of "rm -rf" with "INVALID COMMAND". If "rm -rf" is not present in the input, return the input string as is.
"""

def sanitizeInput(input_str):
    if "rm -rf" in input_str:
        return input_str.replace("rm -rf", "INVALID COMMAND")
    else:
        return input_str