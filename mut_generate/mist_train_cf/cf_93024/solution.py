"""
QUESTION:
Create a function named `add_large_numbers` that takes two string arguments, each representing a large number with up to 10^6 digits. The function should add the two numbers together and return the result as a string without using built-in functions that directly handle large numbers.
"""

def add_large_numbers(num1, num2):
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    
    num2 = num2.zfill(len(num1))
    
    num1 = [int(digit) for digit in num1]
    num2 = [int(digit) for digit in num2]
    
    result = []
    carry = 0
    
    for i in range(len(num1)-1, -1, -1):
        digit_sum = num1[i] + num2[i] + carry
        carry = digit_sum // 10
        result.append(str(digit_sum % 10))
    
    if carry > 0:
        result.append(str(carry))
    
    return ''.join(result[::-1])