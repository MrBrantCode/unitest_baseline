"""
QUESTION:
You have array a that contains all integers from 1 to n twice. You can arbitrary permute any numbers in a.

Let number i be in positions x_{i}, y_{i} (x_{i} < y_{i}) in the permuted array a. Let's define the value d_{i} = y_{i} - x_{i} — the distance between the positions of the number i. Permute the numbers in array a to minimize the value of the sum $s = \sum_{i = 1}^{n}(n - i) \cdot|d_{i} + i - n$.


-----Input-----

The only line contains integer n (1 ≤ n ≤ 5·10^5).


-----Output-----

Print 2n integers — the permuted array a that minimizes the value of the sum s.


-----Examples-----
Input
2

Output
1 1 2 2

Input
1

Output
1 1
"""

def minimize_permutation_sum(n: int) -> list:
    if n % 2 == 0:
        a = []
        for i in range(1, n, 2):
            a.append(i)
        a = a + a[::-1]
        b = []
        for i in range(2, n, 2):
            b.append(i)
        a = a + [n] + b + [n] + b[::-1]
    else:
        a = []
        for i in range(1, n, 2):
            a.append(i)
        a = a + [n] + a[::-1] + [n]
        b = []
        for i in range(2, n, 2):
            b.append(i)
        a = a + b + b[::-1]
    
    return a