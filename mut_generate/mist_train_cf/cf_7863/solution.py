"""
QUESTION:
Write a function called `decimal_to_binary` that takes a non-negative decimal integer as input and returns its binary equivalent as a string. The function should not use any built-in conversion functions or operators to perform the conversion and should have a time complexity of O(log^2 n), where n is the decimal value.
"""

def decimal_to_binary(decimal):
    def divide_by_2(decimal):
        if decimal == 0:
            return ''
        elif decimal % 2 == 0:
            return divide_by_2(decimal // 2) + '0'
        else:
            return divide_by_2(decimal // 2) + '1'

    if decimal == 0:
        return '0'
    binary = divide_by_2(decimal)
    return binary