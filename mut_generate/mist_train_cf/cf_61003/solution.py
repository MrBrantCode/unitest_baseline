"""
QUESTION:
Design a function `add_big_numbers(num1, num2)` that takes two 100-digit numbers as strings `num1` and `num2` and returns their summation as a string. Implement the function without using any built-in functions or libraries that support arbitrary-precision arithmetic. The function should also handle cases where the numbers have different lengths by padding the shorter number with leading zeroes.
"""

def add_big_numbers(num1, num2):
    # Store the carry
    carry = 0 
    result = ''
 
    # Make both the numbers of same length by adding leading zeroes
    len_diff = len(num1) - len(num2) 
    
    if len_diff > 0:
        num2 = '0' * len_diff + num2
    elif len_diff < 0:
        num1 = '0' * abs(len_diff) + num1
 
    for i in range(len(num1)-1, -1, -1):
        temp = (carry + int(num1[i]) + int(num2[i]))
 
        # In case sum of two digits is more than 9, update carry
        if temp >= 10:
            carry = 1
            result = str(temp % 10) + result 
        else:
            carry = 0
            result = str(temp) + result 
 
    # If there is any carry left
    if carry != 0: 
        result = str(carry) + result

    return result.strip()