"""
QUESTION:
Write a function named `sort_by_binary_len_and_divisor` that takes two parameters: a list of positive integers (`arr`) and a divisor (`divisor`). The function should sort `arr` based on the length of the binary representation of each integer and their quotient when divided by `divisor`. In cases where multiple integers have the same binary length, they should be sorted according to their quotient when divided by `divisor`.
"""

def sort_by_binary_len_and_divisor(arr, divisor):
    return sorted(arr, key=lambda x: (len(bin(x))-2, x // divisor))