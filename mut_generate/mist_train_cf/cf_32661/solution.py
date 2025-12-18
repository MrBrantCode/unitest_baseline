"""
QUESTION:
Write a function `duplicateChars` that takes a string of lowercase English letters as input and returns a new string where each character in the original string is duplicated. 

The function should have the following signature: `def duplicateChars(str: str) -> str:`.
"""

def duplicateChars(str: str) -> str:
    duplicated_str = ""
    for char in str:
        duplicated_str += char * 2
    return duplicated_str