"""
QUESTION:
Write a program that extracts n different numbers from the numbers 0 to 9 and outputs the number of combinations that add up to s. Each n number is from 0 to 9, and the same number cannot be used in one combination. For example, if n is 3 and s is 6, the combination of the three numbers totaling 6 is

1 + 2 + 3 = 6
0 + 1 + 5 = 6
0 + 2 + 4 = 6

There are three ways.



Input

Given multiple datasets. For each dataset, n (1 ≤ n ≤ 9) and s (0 ≤ s ≤ 100) are given on one line, separated by a single space. When both n and s are 0, it is the end of the input (in this case, the program is terminated without processing).

The number of datasets does not exceed 50.

Output

For each dataset, output the number of combinations in which the sum of n integers is s on one line.

Example

Input

3 6
3 1
0 0


Output

3
0
"""

def count_combinations(n: int, s: int) -> int:
    """
    Counts the number of combinations of n different integers from 0 to 9 that add up to s.

    Parameters:
    n (int): The number of integers to be selected.
    s (int): The target sum.

    Returns:
    int: The number of combinations that add up to s.
    """
    def dfs(depth: int, prev: int, sum: int) -> int:
        if depth == n:
            return 1 if sum == s else 0
        ret = 0
        for i in range(prev + 1, 10):
            ret += dfs(depth + 1, i, sum + i)
        return ret
    
    if n == 0 and s == 0:
        return 0
    return dfs(0, -1, 0)