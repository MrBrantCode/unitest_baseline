"""
QUESTION:
Write a function `classify_input(num)` that takes an integer as input and returns a string based on the following criteria: 
- If the input is a prime number and a Fibonacci number, return "prime Fibonacci".
- If the input is a prime number and a palindrome, return "prime palindrome".
- If the input is a perfect square and a palindrome, return "square palindrome".
- If the input is a negative prime number and a palindrome, return "negative prime palindrome".
- If the input is zero, return "zero".

Note that the function should handle prime numbers, Fibonacci numbers, perfect squares, and palindromes correctly.
"""

import math

def classify_input(num):
    # Helper function to check if the input is a prime number
    def is_prime(num):
        # 0 and 1 are not prime numbers
        if num < 2:
            return False
        
        # Check for divisibility from 2 to the square root of the number
        for i in range(2, int(math.sqrt(abs(num))) + 1):
            if abs(num) % i == 0:
                return False
        
        return True
    
    # Helper function to check if the input is a Fibonacci number
    def is_fibonacci(num):
        # Check if the number is a perfect square of a Fibonacci number
        return is_perfect_square(5 * num**2 + 4) or is_perfect_square(5 * num**2 - 4)
    
    # Helper function to check if the input is a perfect square
    def is_perfect_square(num):
        # Check if the square root of the number is an integer
        return math.isqrt(abs(num))**2 == abs(num)
    
    # Helper function to check if the input is a palindrome
    def is_palindrome(num):
        # Convert the number to a string and check if it is equal to its reverse
        return str(num) == str(num)[::-1]
    
    # Check if the input is zero
    if num == 0:
        return "zero"
    
    # Check if the input is a prime number
    if is_prime(num):
        # Check if the input is a Fibonacci number
        if is_fibonacci(num):
            return "prime Fibonacci"
        
        # Check if the input is a palindrome
        if is_palindrome(num):
            if num < 0:
                return "negative prime palindrome"
            else:
                return "prime palindrome"
        
    # Check if the input is a perfect square and a palindrome
    if is_perfect_square(num) and is_palindrome(num):
        return "square palindrome"
    
    # If none of the above conditions are met, return None
    return None