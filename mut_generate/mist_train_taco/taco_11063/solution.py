"""
QUESTION:
Input

The only line of input contains three integers a1, a2, a3 (1 ≤ a1, a2, a3 ≤ 20), separated by spaces.

Output

Output a single integer.

Examples

Input

2 3 2


Output

5


Input

13 14 1


Output

14


Input

14 5 9


Output

464


Input

17 18 3


Output

53
"""

def calculate_fibonacci_value(a1: int, a2: int, idx: int) -> int:
    # Initialize the sequence with the given values
    f = [0] * 22
    f[0], f[1] = a1, a2
    
    # Compute the Fibonacci-like sequence
    for i in range(2, 22):
        f[i] = f[i - 1] + f[i - 2]
    
    # Return the value at the specified index
    return f[idx]