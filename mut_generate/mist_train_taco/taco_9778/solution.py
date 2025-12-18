"""
QUESTION:
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:


Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:


Input: num1 = "123", num2 = "456"
Output: "56088"


Note:


       The length of both num1 and num2 is < 110.
       Both num1 and num2 contain only digits 0-9.
       Both num1 and num2 do not contain any leading zero, except the number 0 itself.
       You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

def multiply_strings(num1: str, num2: str) -> str:
    a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    z = 0
    x = 0
    
    # Convert num1 from string to integer
    for i, element in enumerate(num1):
        for j in range(10):
            if element == a[j]:
                z += j * 10 ** (len(num1) - i - 1)
    
    # Convert num2 from string to integer
    for c, b in enumerate(num2):
        for k in range(10):
            if b == a[k]:
                x += k * 10 ** (len(num2) - c - 1)
    
    # Multiply the two integers
    mul = z * x
    
    # Convert the result back to string
    return ''.join('%d' % mul)