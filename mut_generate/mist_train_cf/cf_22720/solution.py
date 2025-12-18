"""
QUESTION:
Implement the function `is_palindrome(num)` that checks whether the input integer `num` is a palindrome. The function should have a time complexity of O(log n), where n is the number of digits in `num`, and use a constant amount of additional space. The function should also handle negative numbers by considering them as palindromes if their absolute values are palindromes. The input number should not be converted to a string or any other data type.
"""

def is_palindrome(num):
    if num < 0:
        num = abs(num)

    num_digits = 0
    temp = num
    while temp > 0:
        num_digits += 1
        temp //= 10
    
    reversed_half = 0
    for _ in range(num_digits // 2):
        reversed_half = (reversed_half * 10) + (num % 10)
        num //= 10
    
    if num_digits % 2 != 0:
        num //= 10
    
    return num == reversed_half