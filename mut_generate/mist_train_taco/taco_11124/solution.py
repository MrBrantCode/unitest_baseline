"""
QUESTION:
Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):

If either input is an empty string, consider it as zero.
"""

def sum_strings(a: str, b: str) -> str:
    return str(int(a or '0') + int(b or '0'))