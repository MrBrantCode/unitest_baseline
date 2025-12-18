"""
QUESTION:
Write a program which identifies the number of combinations of three integers which satisfy the following conditions:

* You should select three distinct integers from 1 to n.
* A total sum of the three integers is x.



For example, there are two combinations for n = 5 and x = 9.

* 1 + 3 + 5 = 9
* 2 + 3 + 4 = 9

Note

解説

Constraints

* 3 ≤ n ≤ 100
* 0 ≤ x ≤ 300

Input

The input consists of multiple datasets. For each dataset, two integers n and x are given in a line.

The input ends with two zeros for n and x respectively. Your program should not process for these terminal symbols.

Output

For each dataset, print the number of combinations in a line.

Example

Input

5 9
0 0


Output

2
"""

def count_combinations(n: int, x: int) -> int:
    count = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if i + j + k == x:
                    count += 1
    return count