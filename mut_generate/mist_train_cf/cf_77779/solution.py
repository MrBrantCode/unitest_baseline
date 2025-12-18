"""
QUESTION:
Create a function "digits" that takes a positive integer n and returns a calculated value based on its digits. The function should handle the following cases:
- If n contains both even and odd digits, return the sum of the squares of its even digits and the sum of the factorials of its odd digits.
- If all digits are even, return the square root of the product of the first half of the even digits.
- If all digits are odd, return the factorial of the sum of the first half of the odd digits.
"""

import math

def digits(n):
    str_n = str(n)
    even_digits = [int(i) for i in str_n if int(i) % 2 == 0]
    odd_digits = [int(i) for i in str_n if int(i) % 2 != 0]
    
    if not even_digits and odd_digits:  # all digits are odd
        half = len(odd_digits) // 2
        return math.factorial(sum(odd_digits[:half]))
    elif not odd_digits and even_digits:  # all digits are even
        half = len(even_digits) // 2
        return math.sqrt(math.prod(even_digits[:half]))
    else:
        return sum([i**2 for i in even_digits]) + sum([math.factorial(i) for i in odd_digits])