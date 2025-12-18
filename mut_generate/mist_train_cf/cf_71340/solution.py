"""
QUESTION:
Write a recursive function named `hello_multiverse` that prints "Hello, Multiverse!" along with a corresponding Fibonacci sequence number to the terminal. The function should print the message exactly 5 times, with each message displaying a new number from the Fibonacci sequence.
"""

def fibonacci(n):
    if n <= 1:
       return n
    else:
       return(fibonacci(n-1) + fibonacci(n-2))

def hello_multiverse(count=0, fib_count=0):
    if count < 5:
        print(f"Hello, Multiverse! Fibonacci sequence: {fibonacci(fib_count)}")
        hello_multiverse(count+1, fib_count+1)