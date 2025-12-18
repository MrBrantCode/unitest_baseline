"""
QUESTION:
Create a Python function 'checkInteger' that takes a number and returns True if the number is an integer within the range of -10^18 to 10^18, False otherwise. The function should handle negative numbers and check for additional properties: whether the number is a perfect square, a prime number, and a palindrome (considering only its absolute value).
"""

import math

def checkInteger(number):
    if isinstance(number, int):
        if -10**18 <= number <= 10**18:
            is_perfect_square = False
            is_prime = False
            is_palindrome = False
            
            if number >= 0:
                sqrt = math.isqrt(number)
                is_perfect_square = sqrt * sqrt == number
            
            if number > 1:
                for i in range(2, int(math.sqrt(abs(number))) + 1):
                    if number % i == 0:
                        is_prime = False
                        break
                else:
                    is_prime = True
            
            if str(abs(number)) == str(abs(number))[::-1]:
                is_palindrome = True
            
            return True, is_perfect_square, is_prime, is_palindrome
        else:
            return False, False, False, False
    else:
        return False, False, False, False