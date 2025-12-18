"""
QUESTION:
Create a function `fibonacci(n)` that generates the Fibonacci series up to the given integer `n`, determines the sum of even Fibonacci numbers within the series, and returns the Fibonacci series and the list of even Fibonacci numbers. The function should not take any additional inputs besides `n`. The Fibonacci series should include 0 and 1 as the first two numbers. The series should only include numbers up to `n`, and the even numbers list should only include numbers that are even.
"""

def fibonacci(n):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    even_fibonacci_numbers = [num for num in fibonacci_sequence if num % 2 == 0]
    return fibonacci_sequence, even_fibonacci_numbers