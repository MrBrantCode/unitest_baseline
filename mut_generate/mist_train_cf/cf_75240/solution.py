"""
QUESTION:
Create a function named `complex_sequence(n)` that generates a sequence of alternating 0s and 1s with intervals determined by the Fibonacci sequence. The function should take an integer `n` as input, representing the desired length of the sequence, and return a list of the generated sequence. The sequence should start with a single 0, followed by a single 1, then two numbers (0, 1), then three numbers (0, 1, 0), and so on, with the length of each interval determined by the corresponding Fibonacci number.
"""

def complex_sequence(n):
    fib = [0, 1]
    seq = []
    while len(seq) < n:
        fib.append(fib[-1] + fib[-2]) # Fibonacci sequence
        # Append 0 and 1 alternatively
        for i in range(fib[-1]):
            if len(seq) < n:
                seq.append(len(seq) % 2)
            else:
                break
    return seq[:n]