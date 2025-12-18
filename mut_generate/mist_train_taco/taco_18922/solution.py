"""
QUESTION:
It's holiday. Mashmokh and his boss, Bimokh, are playing a game invented by Mashmokh. 

In this game Mashmokh writes sequence of n distinct integers on the board. Then Bimokh makes several (possibly zero) moves. On the first move he removes the first and the second integer from from the board, on the second move he removes the first and the second integer of the remaining sequence from the board, and so on. Bimokh stops when the board contains less than two numbers. When Bimokh removes numbers x and y from the board, he gets gcd(x, y) points. At the beginning of the game Bimokh has zero points.

Mashmokh wants to win in the game. For this reason he wants his boss to get exactly k points in total. But the guy doesn't know how choose the initial sequence in the right way. 

Please, help him. Find n distinct integers a1, a2, ..., an such that his boss will score exactly k points. Also Mashmokh can't memorize too huge numbers. Therefore each of these integers must be at most 109.

Input

The first line of input contains two space-separated integers n, k (1 ≤ n ≤ 105; 0 ≤ k ≤ 108).

Output

If such sequence doesn't exist output -1 otherwise output n distinct space-separated integers a1, a2, ..., an (1 ≤ ai ≤ 109).

Examples

Input

5 2


Output

1 2 3 4 5


Input

5 3

Output

2 4 3 7 1

Input

7 2


Output

-1

Note

gcd(x, y) is greatest common divisor of x and y.
"""

def generate_sequence(n, k):
    if k < 0 or (n < 2 and k > 0):
        return -1
    
    x = k - (n // 2 - 1)
    if x < 1:
        return -1
    
    sequence = [0] * n
    sequence[0] = x
    
    if n > 1:
        sequence[1] = 2 * x
    
    if n >= 3:
        newValue = 1
        while newValue == x or newValue == 2 * x or newValue + 1 == x or (newValue + 1 == 2 * x):
            newValue += 1
        sequence[2] = newValue
    
    for i in range(3, n):
        newValue = sequence[i - 1] + 1
        if not i & 1:
            while newValue == x or newValue == 2 * x or newValue + 1 == x or (newValue + 1 == 2 * x):
                newValue += 1
        sequence[i] = newValue
    
    return sequence