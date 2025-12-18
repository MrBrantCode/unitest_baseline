"""
QUESTION:
It is known that fleas in Berland can jump only vertically and horizontally, and the length of the jump is always equal to s centimeters. A flea has found herself at the center of some cell of the checked board of the size n × m centimeters (each cell is 1 × 1 centimeters). She can jump as she wishes for an arbitrary number of times, she can even visit a cell more than once. The only restriction is that she cannot jump out of the board.

The flea can count the amount of cells that she can reach from the starting position (x, y). Let's denote this amount by dx, y. Your task is to find the number of such starting positions (x, y), which have the maximum possible value of dx, y.

Input

The first line contains three integers n, m, s (1 ≤ n, m, s ≤ 106) — length of the board, width of the board and length of the flea's jump.

Output

Output the only integer — the number of the required starting positions of the flea.

Examples

Input

2 3 1000000


Output

6


Input

3 3 2


Output

4
"""

def count_max_reachable_positions(n: int, m: int, s: int) -> int:
    r = -(-n // s) * (s if n % s == 0 else n % s)
    c = -(-m // s) * (s if m % s == 0 else m % s)
    return r * c