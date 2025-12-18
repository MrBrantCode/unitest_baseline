"""
QUESTION:
Create a function called `add` that takes two integer arrays of unequal length, each representing a large number where each integer is a digit. The function should add these two numbers together and return the sum as an array of digits, handling any carry from each digit addition. The function should be able to handle large numbers with a magnitude greater than the standard integer data type.
"""

def add(num1, num2):
    # Make sure num1 is the longer number
    if len(num1) < len(num2):
        num1, num2 = num2, num1

    num1 = num1[::-1]
    num2 = num2[::-1]

    carry = 0
    result = []

    # Add each digit, considering the carry
    for i in range(len(num1)):
        total = carry
        total += num1[i]
        if i < len(num2):
            total += num2[i]
        result.append(total % 10)
        carry = total // 10

    # Handle the possible remaining carry
    if carry != 0:
        result.append(carry)
        
    return result[::-1]