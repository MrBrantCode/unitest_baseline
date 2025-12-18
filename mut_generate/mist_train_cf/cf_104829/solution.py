"""
QUESTION:
The function, named 'arithmetic_operation', takes two parameters 'a' and 'b'. It should perform addition, subtraction, multiplication, and division operations using these two numbers, then return the results. The division result should be rounded to the nearest integer. Note that 'a' and 'b' are integers and 'b' is not zero.
"""

def arithmetic_operation(a, b):
    sum_result = a + b
    difference = a - b
    product = a * b
    quotient = round(a / b)
    return sum_result, difference, product, quotient