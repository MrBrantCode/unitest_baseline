"""
QUESTION:
Write a function `isPalindrome` to determine if a given integer `x` is a palindrome without converting it to a string. An integer is a palindrome when it reads the same backward as forward. The function should handle negative integers and potential integer overflow when reversing the integer. It should return a boolean value indicating whether `x` is a palindrome or not.
"""

def isPalindrome(x: int) -> bool:
    # Handle negative integers and numbers ending with 0
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    # Reverse half of the number and compare with the other half
    reversed_num = 0
    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    
    # For odd-length numbers, handle the middle digit
    return x == reversed_num or x == reversed_num // 10