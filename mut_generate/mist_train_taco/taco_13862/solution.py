"""
QUESTION:
<image>

Input

The input contains a single integer a (1 ≤ a ≤ 18257).

Output

Print a single integer output (1 ≤ output ≤ 2·109).

Examples

Input

2


Output

13
"""

def calculate_star_sequence_value(a):
    (current_value, increment) = (1, 12)
    for i in range(2, a + 1):
        current_value += increment
        increment += 12
    return current_value