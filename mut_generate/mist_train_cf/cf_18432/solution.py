"""
QUESTION:
Create a function `fibonacci_sequence(n)` that prints a Fibonacci sequence up to the nth term and returns the sum of all the numbers in the sequence, given that n is a positive integer greater than or equal to 3, without using recursion or built-in Fibonacci functions/libraries.
"""

def fibonacci_sequence(n):
    fib_seq = [0, 1]  
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])  
    for term in fib_seq:
        print(term)
    return sum(fib_seq)