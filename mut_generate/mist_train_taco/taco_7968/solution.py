"""
QUESTION:
Write a program which prints multiplication tables in the following format:


1x1=1
1x2=2
.
.
9x8=72
9x9=81




Input

No input.

Output


1x1=1
1x2=2
.
.
9x8=72
9x9=81


Example

Input




Output
"""

def generate_multiplication_table(start_range=1, end_range=9):
    table = []
    for i in range(start_range, end_range + 1):
        for j in range(start_range, end_range + 1):
            table.append(f"{i}x{j}={i * j}")
    return table