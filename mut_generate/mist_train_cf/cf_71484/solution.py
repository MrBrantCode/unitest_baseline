"""
QUESTION:
Create a function `analyze_numbers` that takes a list of integers as input and returns a dictionary where each key is a number from the input list, and its corresponding value is a tuple of two boolean values. The first boolean in the tuple indicates whether the number is a palindrome, and the second boolean indicates whether the number is prime. The function should be efficient enough to handle a large set of numbers.
"""

def analyze_numbers(numbers):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    result = {}
    for number in numbers:
        result[number] = (is_palindrome(number), is_prime(number))
    return result