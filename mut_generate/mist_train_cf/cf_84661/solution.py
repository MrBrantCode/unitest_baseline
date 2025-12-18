"""
QUESTION:
Create a function `isPalindrome(x)` that takes an integer `x` as input and returns a boolean value indicating whether the integer is a palindrome. A palindrome is a number that reads the same forwards and backwards. The function should work with integers in the range `-2^31 <= x <= 2^31 - 1`. The solution should not convert the integer into a string.
"""

def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    revertedNumber = 0
    while x > revertedNumber:
        revertedNumber = revertedNumber * 10 + x % 10
        x //= 10
    return x == revertedNumber or x == revertedNumber // 10