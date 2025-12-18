"""
QUESTION:
Write a function `xor_binary_numbers(a, b)` that takes two binary strings `a` and `b` of the same length `n` as input and returns a list of strings representing the exclusive OR (XOR) of the two binary numbers. The function should only use bitwise operators and have a time complexity of O(n).
"""

def xor_binary_numbers(a, b):
    result = []
    for i in range(len(a)):
        bit_a = int(a[i])
        bit_b = int(b[i])
        xor_result = bit_a ^ bit_b
        result.append(str(xor_result))
    return result