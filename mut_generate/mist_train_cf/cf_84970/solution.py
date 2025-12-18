"""
QUESTION:
Write a function named `fibonacci_sum` that calculates the sum of the Fibonacci numbers up to the nth number, using both iterative and recursive methods. The function should handle edge cases where the provided input `n` is less than or equal to 0.
"""

# Function to calculate the sum of the Fibonacci numbers up to the nth number using both iterative and recursive methods.

# Iterative method to solve fibonacci sum
def fibonacci_sum(n):
    # handle edge cases
    if n <= 0: 
        return "Input should be positive"
    elif n == 1: 
        return 1
    else:
        sum = 1
        num1 = 1
        num2 = 1
        for i in range(3, n+1):
            temp = num1 + num2
            sum += temp
            num2 = num1
            num1 = temp
        return sum

# Recursive method to solve fibonacci sum
def fibonacci_sum(n):
    # handle edge cases
    if n <= 0: 
        return "Input should be positive"
    elif n == 1: 
        return 1
    elif n == 2: 
        return 2
    else:
        return fibonacci_sum(n-1) + fibonacci(n)
        
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)