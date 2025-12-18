"""
QUESTION:
Write a function called `factorials_up_to_n` that prints the factorial of all numbers from 1 to a given integer n. Implement this function using both recursive and iterative approaches, and consider optimizing for runtime efficiency. Assume n is a non-negative integer.
"""

def factorials_up_to_n_recursive(n):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    for i in range(1, n+1):
        print(f"Factorial of {i} is {factorial(i)}")

def factorials_up_to_n_iterative(n):
    for i in range(1, n+1):
        factorial = 1
        for j in range(1, i+1):
            factorial *= j
        print(f"Factorial of {i} is {factorial}")

def factorials_up_to_n_dp(n):
    factorials = [1] * (n + 1)
    for i in range(1, n + 1):
        factorials[i] = i * factorials[i - 1]
    for i in range(1, n+1):
        print(f"Factorial of {i} is {factorials[i]}")