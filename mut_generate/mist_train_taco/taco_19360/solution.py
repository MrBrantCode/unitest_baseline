"""
QUESTION:
While resting on the ship after the "Russian Code Cup" a boy named Misha invented an interesting game. He promised to give his quadrocopter to whoever will be the first one to make a rectangular table of size n × m, consisting of positive integers such that the sum of the squares of numbers for each row and each column was also a square.

Since checking the correctness of the table manually is difficult, Misha asks you to make each number in the table to not exceed 108.

Input

The first line contains two integers n and m (1 ≤ n, m ≤ 100) — the size of the table. 

Output

Print the table that meets the condition: n lines containing m integers, separated by spaces. If there are multiple possible answers, you are allowed to print anyone. It is guaranteed that there exists at least one correct answer.

Examples

Input

1 1


Output

1

Input

1 2


Output

3 4
"""

def generate_magic_table(n, m):
    def sqr(n):
        if n == 1:
            return [1]
        if n == 2:
            return [4, 3]
        if n % 2:
            return [(n + 1) // 2, 2] + [1] * (n - 2)
        return [(n - 2) // 2] + [1] * (n - 1)
    
    a = sqr(n)
    b = sqr(m)
    
    table = []
    for i in range(n):
        row = [a[i] * x for x in b]
        table.append(row)
    
    return table