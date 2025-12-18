"""
QUESTION:
Petya loves lucky numbers. We all know that lucky numbers are the positive integers whose decimal representations contain only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Petya wonders eagerly what minimum lucky number has the sum of digits equal to n. Help him cope with the task.

Input

The single line contains an integer n (1 ≤ n ≤ 106) — the sum of digits of the required lucky number.

Output

Print on the single line the result — the minimum lucky number, whose sum of digits equals n. If such number does not exist, print -1.

Examples

Input

11


Output

47


Input

10


Output

-1
"""

def find_min_lucky_number(n: int) -> str:
    i = 0
    j = 0
    while n >= 0:
        if n % 7 == 0:
            j = n // 7
            ans = ['4'] * i + ['7'] * j
            return ''.join(ans)
        n -= 4
        i += 1
    return '-1'