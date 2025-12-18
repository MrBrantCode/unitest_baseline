"""
QUESTION:
Create a function `print_fibonacci(n)` that generates a Fibonacci sequence starting from the nth term and prints it in reverse order if n is odd, and in regular order if n is even. The output should include the original value of n, the Fibonacci sequence, and whether it was printed in reverse or regular order. Additionally, the function should verify that the generated sequence is correct for the given value of n.
"""

def print_fibonacci(n):
    def fibonacci(i):
        if i <= 1:
            return i
        else:
            return fibonacci(i-1) + fibonacci(i-2)

    fib_sequence = []
    for i in range(n, -1, -1):
        fib_sequence.append(fibonacci(i))

    if n % 2 == 0:
        print(f"Fibonacci sequence starting from {n} in regular order: {fib_sequence}")
    else:
        print(f"Fibonacci sequence starting from {n} in reverse order: {fib_sequence[::-1]}")

    correct_sequence = [fibonacci(i) for i in range(n+1)]
    if fib_sequence == correct_sequence:
        print("The generated sequence is correct.")
    else:
        print("The generated sequence is incorrect.")