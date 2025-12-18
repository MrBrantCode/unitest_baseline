"""
QUESTION:
Create a Python function 'checkInteger' that takes a number and returns True if the number is an integer within the range of -10^18 to 10^18, and False otherwise. 

Additionally, create three more functions: 'isPerfectSquare', 'isPrime', and 'isPalindrome', which should check if the input number is a perfect square, a prime number, and a palindrome respectively. 

The 'isPalindrome' function should consider only the absolute value of the input number. The 'isPerfectSquare' and 'isPrime' functions should return False for negative numbers. The functions should handle edge cases and other constraints.
"""

import math

def checkInteger(number):
    if isinstance(number, int):
        if -10**18 <= number <= 10**18:
            return True
        else:
            return False
    else:
        return False

def isPerfectSquare(number):
    if checkInteger(number):
        if number >= 0:
            sqrt = math.isqrt(number)
            return sqrt * sqrt == number
        else:
            return False
    else:
        return False

def isPrime(number):
    if checkInteger(number):
        if number <= 1:
            return False
        for i in range(2, int(math.sqrt(abs(number))) + 1):
            if number % i == 0:
                return False
        return True
    else:
        return False

def isPalindrome(number):
    if checkInteger(number):
        if str(abs(number)) == str(abs(number))[::-1]:
            return True
        else:
            return False
    else:
        return False