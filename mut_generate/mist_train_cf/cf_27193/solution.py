"""
QUESTION:
Create a function named `find_invalid_function_names` that takes a list of function names as input. The function should return a list of names that do not follow the snake_case naming convention or start with the word "without". All function names should be in lowercase and should not contain uppercase letters.
"""

from typing import List

def find_invalid_function_names(function_names: List[str]) -> List[str]:
    invalid_names = []
    for name in function_names:
        if not name.islower() or name.startswith("without"):
            invalid_names.append(name)
    return invalid_names