"""
QUESTION:
Create a function named `even_odd_count` that takes an integer as input and returns a tuple containing the count of even and odd digits in the integer. The function should handle both positive and negative integers, ignoring the sign. For example, `even_odd_count(-12)` should return `(1, 1)` and `even_odd_count(123)` should return `(1, 2)`.
"""

def even_odd_count(num):
    even_count = 0
    odd_count = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count