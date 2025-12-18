"""
QUESTION:
Compose a function called `sophisticated_function` that takes two parameters, `my_string` and `letter`, and returns a string with all instances of `letter` removed from `my_string`. The function should preserve the original grammar and syntax of the input string.
"""

def sophisticated_function(my_string: str, letter: str) -> str:
    # replace the letter with empty character
    return my_string.replace(letter, '')