"""
QUESTION:
Implement a function named 'multiply_list_elements' that takes a list of integers as input, multiplies all the elements in the list, and returns the result. The function must only use addition, subtraction, and bit shifting operations, without relying on the '*' operator or built-in multiplication functions. The list may contain both positive and negative integers.
"""

def multiply_list_elements(my_list):
    def multiply(a, b):
        result = 0
        is_negative = (a < 0) ^ (b < 0)
        a, b = abs(a), abs(b)
        while b != 0:
            if b & 1:
                result += a
            a <<= 1
            b >>= 1
        return -result if is_negative else result

    result = 1
    for num in my_list:
        result = multiply(result, num)
    return result