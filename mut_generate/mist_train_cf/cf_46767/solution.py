"""
QUESTION:
Write a function named `print_fibonacci(n)` that prints the first `n` Fibonacci numbers in descending order. The function should handle the case where `n` is a negative integer by printing an error message.
"""

def print_fibonacci(n):
    # Check if the input number is negative
    if n < 0:
        print("Error: N cannot be a negative number!")
        return
    if n == 1:
        print("1")
        return
    a, b = 0, 1
    fib = []
    fib.append(a)
    fib.append(b)
    for i in range(2,n):
        a, b = b, a+b
        fib.append(b)
    # Print the Fibonacci numbers in descending order
    for i in fib[::-1]:
        print(i, end=" ")