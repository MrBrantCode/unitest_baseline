"""
QUESTION:
Write a function `multiply_binary_nums_binary_shifts` that takes two integers `num1` and `num2` as input and returns their product without using any built-in multiplication operators or functions. The function should be able to handle 64-bit binary numbers.
"""

def multiply_binary_nums_binary_shifts(num1, num2):
    result = 0
    while num2 > 0:
        if num2 & 1:
            result += num1
        num1 = num1 << 1
        num2 = num2 >> 1
    return result