"""
QUESTION:
Implement the `process_text(input_string)` function, which takes a string `input_string` as input and returns the modified string with the following transformations: 
- Replace all occurrences of "With output:" with "Processed output:".
- Replace all occurrences of "--------------" with "==============".
- Replace all occurrences of "frombytes" with "tostring".
"""

def entrance(input_string):
    modified_string = input_string.replace("With output:", "Processed output:")
    modified_string = modified_string.replace("--------------", "==============")
    modified_string = modified_string.replace("frombytes", "tostring")
    return modified_string