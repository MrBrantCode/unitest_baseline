"""
QUESTION:
Create a function named `append_string` that takes two parameters: `input_str` and `arr`. This function should check if `input_str` contains the phrase "hello world". If it does, append `input_str` to `arr`. If it does not, append "not found" to `arr`. The function must return the updated `arr`.
"""

def append_string(input_str, arr):
    if "hello world" in input_str:
        arr.append(input_str)
    else:
        arr.append("not found")
    return arr