"""
QUESTION:
Create a function `classify_input(number)` that takes an integer as input and returns its classification based on the following criteria: 
- prime Fibonacci palindrome: if the input is a prime number, a Fibonacci number, and a palindrome
- prime palindrome: if the input is a prime number and a palindrome
- square palindrome: if the input is a perfect square and a palindrome
- negative prime palindrome: if the input is a negative prime number and a palindrome
- zero: if the input is zero.
The input number must be a positive integer within the range of 1 to 1000 (inclusive).
"""

def classify_input(number):
    # Check if input is within the specified range
    if number < 1 or number > 1000:
        return "Input must be a positive integer within the range of 1 to 1000."
    
    # Check if input is zero
    if number == 0:
        return "zero"
    
    # Check if input is a prime number
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # Check if input is a palindrome
    def is_palindrome(n):
        return str(n) == str(n)[::-1]
    
    # Check if input is a Fibonacci number
    def is_fibonacci(n):
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        return b == n
    
    # Check the conditions and return the corresponding classification
    if is_prime(number) and is_fibonacci(number) and is_palindrome(number):
        return "prime Fibonacci palindrome"
    elif is_prime(number) and is_palindrome(number):
        return "prime palindrome"
    elif int(number ** 0.5) ** 2 == number and is_palindrome(number):
        return "square palindrome"
    elif is_prime(-number) and is_palindrome(number):
        return "negative prime palindrome"