"""
QUESTION:
Create a Python function called `wrap_bold_tag` that takes a string as input and returns the string with the first occurrence of the word "bold" wrapped in a `<strong>` HTML tag. The input string will always contain at least one occurrence of the word "bold".
"""

def wrap_bold_tag(string):
    index = string.index("bold")
    wrapped_string = string[:index] + "<strong>" + "bold" + "</strong>" + string[index+4:]
    return wrapped_string