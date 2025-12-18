"""
QUESTION:
Write a program that extracts n different numbers from the numbers 0 to 100 and outputs the number of combinations that add up to s. Each n number is from 0 to 100, and the same number cannot be used in one combination. For example, if n is 3 and s is 6, the combination of the three numbers totaling 6 is


1 + 2 + 3 = 6
0 + 1 + 5 = 6
0 + 2 + 4 = 6


There are three ways.



Input

Given multiple datasets. For each dataset, n (1 ≤ n ≤ 9) and s (0 ≤ s ≤ 1000) are given on one line, separated by a space. When both n and s are 0, it is the end of the input.

The number of datasets does not exceed 50.

Output

For each dataset, output the number of combinations in which the sum of n integers is s on one line.

No input is given with more than 1010 combinations.

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
    Counts the number of combinations of n different integers from 0 to 100 that sum up to s.

    Parameters:
    n (int): The number of integers to use in the combination.
    s (int): The target sum.

    Returns:
    int: The number of valid combinations.
    """
    # Precompute the DP table
    dp = [[0 for _ in range(1001)] for _ in range(10)]
    dp[0][0] = 1
    
    for now in range(1, 101):
        for used in range(9, 0, -1):
            dpu = dp[used]
            dpu_1 = dp[used - 1]
            for s_val in range(now, 1001):
                dpu[s_val] = dpu_1[s_val - now] + dpu[s_val]
    
    # Return the result for the given n and s
    return dp[n][s]