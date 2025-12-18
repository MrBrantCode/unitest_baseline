"""
QUESTION:
Write a function `solution` that takes the binary representation of a positive integer `n` as a string and returns the length of the longest consecutive sequence of ones in the binary representation. The input string will only contain the digits '0' and '1'. The function should return an integer value.
"""

def solution(n):
    binary_n = bin(n)[2:]
    max_count = 0
    count = 0
    for digit in binary_n:
        if digit == '1':
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count