"""
QUESTION:
Create a program with three functions: `fibonacci(n)`, `gcd(a, b)`, and `main()`. The `fibonacci(n)` function should calculate the nth Fibonacci number where n is a positive integer. The `gcd(a, b)` function should calculate the greatest common divisor between two numbers a and b. The `main()` function should get user input for a positive integer n, calculate the nth and (n+1)th Fibonacci numbers, and the greatest common divisor between them. Ensure the program handles invalid user input and provide the calculated Fibonacci numbers and GCD.
"""

def fibonacci(n):
    """
    Calculate the nth fibonacci number.
    """
    if n <= 0:
        print("Number should be a positive integer.")
        return None
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < n + 1:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return fibonacci_numbers[n]