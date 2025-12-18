"""
QUESTION:
Create a function `convert_list` that takes a list containing both strings and integers as input. The function should identify the strings in the list, convert them to uppercase without using any built-in Python method or function for uppercase conversion, and replace the original strings in the list with their uppercase versions. The integers in the list should remain unchanged.
"""

def convert_list(lst):
    lower_to_upper = {chr(i): chr(i - 32) for i in range(ord('a'), ord('z')+1)}
    return ["".join(lower_to_upper.get(ch, ch) for ch in s) if type(s) == str else s for s in lst]