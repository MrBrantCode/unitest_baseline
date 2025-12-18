"""
QUESTION:
Write a function `fibonacci(n)` to generate a Fibonacci sequence up to the nth term, and another function `sum_of_even_numbers(numbers)` to find the sum of all even-valued terms in the sequence. The function should handle large numbers up to the 50th term.
"""

def fibonacci(n):
    """Generate a Fibonacci sequence up to the nth term"""
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < n:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return fibonacci_numbers

def sum_of_even_numbers(numbers):
    """Return the sum of all even-valued terms in the sequence"""
    return sum(number for number in numbers if number % 2 == 0)