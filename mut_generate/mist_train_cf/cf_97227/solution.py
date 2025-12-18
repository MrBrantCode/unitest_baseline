"""
QUESTION:
Write a function `is_palindrome(num)` that checks whether the given integer `num` is a palindrome or not. The function should have a time complexity of O(log n), where n is the number of digits in the input number, and use a constant amount of additional space. It should handle negative numbers by considering their absolute values and not convert the input number to a string or any other data type.
"""

def is_palindrome(num):
    if num < 0:
        num = abs(num)
    
    # Find the number of digits in the input number
    num_digits = 0
    temp = num
    while temp > 0:
        num_digits += 1
        temp //= 10
    
    # Reverse half of the number and compare it with the other half
    reversed_half = 0
    for _ in range(num_digits // 2):
        reversed_half = (reversed_half * 10) + (num % 10)
        num //= 10
    
    # If the number has odd digits, ignore the middle digit
    if num_digits % 2 != 0:
        num //= 10
    
    return num == reversed_half