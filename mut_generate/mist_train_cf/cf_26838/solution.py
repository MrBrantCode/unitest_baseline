"""
QUESTION:
Implement the `manipulate_string` function, which takes a string as input and returns the modified string after applying the following rules: converting to lowercase, replacing all 'e' with '3', replacing all 's' with '$', and appending '123' to the end. The function should return a string.
"""

def manipulate_string(input_string: str) -> str:
    modified_string = input_string.lower()
    modified_string = modified_string.replace('e', '3')
    modified_string = modified_string.replace('s', '$')
    modified_string += '123'
    return modified_string