"""
QUESTION:
Write a function called `decimal_to_binary` that takes an integer as input and returns its binary equivalent as a string. Do not use any built-in conversion functions or operators to perform the conversion. The function should have a time complexity of O(log^2 n), where n is the decimal value.
"""

def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'

    def divide_by_2(decimal):
        if decimal == 0:
            return ''
        elif decimal % 2 == 0:
            return divide_by_2(decimal // 2) + '0'
        else:
            return divide_by_2(decimal // 2) + '1'

    binary = divide_by_2(decimal)
    return binary