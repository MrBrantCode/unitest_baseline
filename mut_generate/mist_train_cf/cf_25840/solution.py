"""
QUESTION:
Write a function `gen_binary_strings(n)` that generates all possible binary strings of a given length `n`. The function should return a list of strings, each containing either '0' or '1', and should not include any strings with a length less than `n`.
"""

def generate_binary_strings(n):
    result = []
    for i in range(2**n):
        s = bin(i)[2:]
        s = s.zfill(n)
        result.append(s)
    return result