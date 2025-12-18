"""
QUESTION:
Create a function `extract_brackets(s)` that takes a string `s` as input. The function should parse the string and extract characters enclosed within different types of brackets (curly, angle, square, and round) and return a dictionary where the keys represent the type of bracket and the values are lists of strings representing the content within each bracket. If the brackets in the string are mismatched, the function should return the string "Mismatched brackets".
"""

import re
from collections import defaultdict

def extract_brackets(s):
    """
    Extract characters enclosed within different types of brackets in a given string.

    Args:
        s (str): The input string to parse.

    Returns:
        dict: A dictionary where keys represent the type of bracket and values are lists of strings representing the content within each bracket.
        str: "Mismatched brackets" if the brackets in the string are mismatched.
    """
    brackets = {"curly": [], "angle": [], "square": [], "round": []}
    escape_sequences = {'{':'curly','}':'curly','(':'round',')':'round','<':'angle','>':'angle','[':'square',']':'square'}
    open_brackets = ['{', '(', '<', '[']
    close_brackets = ['}', ')', '>', ']']

    stack = []
    for i in s:
        if i in open_brackets:
            stack.append(i)
            brackets[escape_sequences[i]].append("")
        elif i in close_brackets:
            if len(stack) == 0 or open_brackets[close_brackets.index(i)] != stack[-1]:
                return "Mismatched brackets"
            else: 
                stack.pop()
        elif len(stack) > 0:
            brackets[escape_sequences[stack[-1]]][-1] += str(i)

    if len(stack) != 0:
        return "Mismatched brackets"

    return brackets