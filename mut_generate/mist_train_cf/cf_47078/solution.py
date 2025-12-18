"""
QUESTION:
Write a function called `extract_odd_and_factorial` that takes a positive integer `n` as input, generates an array of size `n` containing all positive integers up to and including `n`, extracts all odd numbers from the array, and performs a factorial operation on them. The function should handle edge cases where `n` is 0 or 1.
"""

def extract_odd_and_factorial(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    else:
        # Generating array of size "n"
        array = list(range(1, n+1))
        
        # constructs a new list containing all odd numbers
        odd_numbers = [num for num in array if num % 2 != 0]

        # Perform a factorial operation on odd numbers
        factorial_numbers = [factorial(num) for num in odd_numbers]
        return factorial_numbers

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)