"""
QUESTION:
Write a function `count_and_convert(start)` that takes an integer `start` as input and returns the sum of all even numbers from `start` to 10 (inclusive) while printing each even number in both decimal and binary formats. The function should skip odd numbers and only iterate up to 10.
"""

def count_and_convert(start):
    total = 0
    for i in range(start, 11, 2):
        if i % 2 == 0:
            total += i
            print(f"{i} in decimal is {i:d} and in binary is {bin(i)[2:]}")
    return total