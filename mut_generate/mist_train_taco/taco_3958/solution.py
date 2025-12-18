"""
QUESTION:
Chef likes inequalities. Please help him to solve next one.
Given four integers a, b, c, d. Find number of solutions x < y, where a ≤ x ≤ b and c ≤ y ≤ d and x, y integers.

-----Input-----
The first line contains an integer T denoting number of tests.
First line of each test case contains four positive integer numbers a, b, c and d.

-----Output-----
For each test case, output a single number each in separate line denoting number of integer solutions as asked in the problem.

-----Constraints-----
- 1 ≤ T ≤ 20 
- 1 ≤ a, b, c, d ≤ 106 

-----Subtasks-----
- Subtask #1: (30 points)  1 ≤ a, b, c, d ≤ 103.
- Subtask #2: (70 points)  Original constraints.

-----Example-----
Input:1
2 3 3 4

Output:3

Input:1
2 999999 1 1000000

Output:499998500001
"""

def count_integer_solutions(a, b, c, d):
    x = c - a
    n1 = b - a + 1
    n2 = d - c + 1
    s = 0
    
    if x <= 0:
        t = n2 - abs(x) - 1
        for j in range(t, max(0, d - b - 1), -1):
            s += j
    if x > 0:
        t = n2
        for j in range(x, max(0, c - b - 1), -1):
            s += t
        if c - b <= 0:
            for j in range(t - 1, max(0, d - b - 1), -1):
                s += j
    
    return s