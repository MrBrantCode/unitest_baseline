"""
QUESTION:
Write a function `generate_lexico_strings` that takes a string `a_string` and an integer `n` as input, and returns a list of `n` lexicographically ordered strings based on the characters in `a_string`. The function should generate `n` strings, each containing the characters of `a_string` in lexicographical order. The function should return a list of these strings.
"""

def generate_lexico_strings(a_string, n):
    lexico_string = []
    for i in range(n):
        sorted_string = ''.join(sorted(a_string))
        lexico_string.append(sorted_string)
    return lexico_string