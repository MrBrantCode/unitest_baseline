"""
QUESTION:
Create a function named `fibonacci(n)` to print the nth number in the Fibonacci sequence. The function should use a recursive helper function to generate the sequence. The input `n` should be a positive integer and the function should handle invalid inputs. The Fibonacci sequence should start from 0 and terminate if the sequence reaches a number greater than 1000. If `n` is 0 or 1, the function should handle these cases separately without relying on the recursive helper function.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1000:
        return "The fibonacci sequence exceeds 1000."
    else:
        sequence = [0, 1]
        while len(sequence) <= n:
            next_number = sequence[-1] + sequence[-2]
            if next_number > 1000:
                return "The fibonacci sequence exceeds 1000."
            sequence.append(next_number)
        return sequence[n]