"""
QUESTION:
Write a recursive function called `number_to_string` that converts any integer to a string. The function should be able to handle both positive and negative integers. The input number can be any integer, and the function should only use recursion to convert the number to a string.
"""

def number_to_string(num):
    if num < 0:
        return '-' + number_to_string(-num)
    elif num < 10:
        return str(num)
    else:
        return number_to_string(num // 10) + str(num % 10)