"""
QUESTION:
Create a recursive function named int_to_string that takes an integer n as input and returns its string representation. The function should handle negative integers by prepending a minus sign to the result. If the input integer is non-negative, the function should recursively divide the number by 10, convert the remainder to its corresponding character, and concatenate it with the result of the recursive call on the quotient.
"""

def int_to_string(n):
    if n < 0:
        return '-' + int_to_string(-n)
    if n < 10:
        return chr(ord('0') + n)
    return int_to_string(n // 10) + chr(ord('0') + n % 10)