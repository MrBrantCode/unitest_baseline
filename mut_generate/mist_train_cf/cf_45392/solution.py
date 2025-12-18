"""
QUESTION:
Write a function `find_in_fibonacci(n)` that takes a positive integer `n` as input and returns its index in the Fibonacci sequence if `n` exists in the sequence. If `n` does not exist in the sequence, return "None". The function should also include error handling for non-positive integers and non-integer inputs. The index returned should be zero-based, corresponding to the position in the Fibonacci sequence.
"""

def find_in_fibonacci(n):
    if not isinstance(n, int) or n <= 0:
        return "Error: Input is not a positive integer"
    
    fibonacci_seq = [0, 1]
    i = 2
    while fibonacci_seq[-1] < n:
        fibonacci_seq.append(fibonacci_seq[i-1] + fibonacci_seq[i-2])
        i += 1

    if n == fibonacci_seq[-1]:
        return len(fibonacci_seq) - 1

    return None