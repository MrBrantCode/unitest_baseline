"""
QUESTION:
Create a function named `reverse_fibonacci` that takes an integer `n` as input, computes the Fibonacci sequence up to `n` numbers, and prints the sequence in reverse order without using any built-in reverse functions. The function should handle invalid inputs (n <= 0) and only print the sequence for valid inputs (n > 0).
"""

def reverse_fibonacci(n):
    a = 0
    b = 1
    fib_sequence = []

    # First two numbers in fibonacci sequence
    if n <= 0:
        return "Invalid Input. The input number should be greater than 0."
    elif n == 1:
        fib_sequence.append(a)
    else:
        fib_sequence.extend([a, b])  

    # remaining numbers
    for i in range(2, n):
        fib_number = a + b
        fib_sequence.append(fib_number)
        # update values
        a = b
        b = fib_number

    # print the sequence in reverse order
    for i in range(n-1, -1, -1):
        print(fib_sequence[i], end=" ")