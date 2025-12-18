"""
QUESTION:
Create a function called `reverse_string` that takes a string `string` and an integer `n` as inputs. The function should return a string containing the first `n` characters of the input `string` in reverse order. If the input string's length is less than `n`, the function should return the reversed string.
"""

def entance(string, n):
    reversed_string = string[:n][::-1]
    return reversed_string