"""
QUESTION:
The penultimate task involved the calculation of the typical Fibonacci sequence up to the nth term.

Input – single integer n

Output – Fibonacci sequence up to the nth term, all terms on a new line

SAMPLE INPUT
5

SAMPLE OUTPUT
1
1
2
3
5
"""

def generate_fibonacci_sequence(n: int) -> list:
    if n <= 0:
        return []
    
    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(b)
        a, b = b, a + b
    
    return sequence