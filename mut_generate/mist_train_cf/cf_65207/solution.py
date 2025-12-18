"""
QUESTION:
Write a function named `fib` that generates the Fibonacci sequence up to the first term with "n" digits. The function should handle potential overflow errors for large inputs. The input "n" represents the number of digits in the last term of the sequence, not the number of terms in the sequence. The function should return the generated Fibonacci sequence.
"""

def fib(n):
    fib_sequence = [0, 1]
    while len(str(fib_sequence[-1])) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        
    return fib_sequence