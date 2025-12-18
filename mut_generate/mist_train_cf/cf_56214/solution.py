"""
QUESTION:
Create a function named `generate_string` that generates a string of length 100 by recursively doubling the length of the input string, without using loops. The function should take a string `s` as input and return a string of length 100. The solution should be efficient and avoid exceeding the maximum recursion depth.
"""

def generate_string(s):
    if len(s) >= 100:
        return s[:100]
    else:
        return generate_string(s + s)