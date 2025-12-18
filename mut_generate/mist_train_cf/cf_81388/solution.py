"""
QUESTION:
Implement a function `num_operation` that takes one argument, a number. The function should deduct 10 from the number if it is odd and a positive integer, otherwise multiply the number by 2 if it is an even positive integer. If the number is not a positive integer, the function should return "Invalid!"
"""

def num_operation(num):
    return num - 10 if isinstance(num, int) and num > 0 and num % 2 != 0 else num * 2 if isinstance(num, int) and num > 0 else "Invalid!"