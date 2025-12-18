"""
QUESTION:
Write a function `checkEvenOrOdd(num)` to determine whether a given number is even or odd. The function should handle both integer and floating point numbers. For floating point numbers, consider them even if they can be expressed as 2n and odd if they can be expressed as 2n+1, where n is an integer. The function should not use the modulo (%) operator, division (/) operator, or the built-in Python function `isinstance()`.
"""

def checkEvenOrOdd(num):
    # handle negative numbers
    num = abs(num)
    if num - int(num) != 0:
        return "Number is not an integer"
    elif (int(num) & 1) == 0:
        return "Even"
    else:
        return "Odd"