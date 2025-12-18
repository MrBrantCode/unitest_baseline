"""
QUESTION:
Consider a sequence of n numbers using integers from 0 to 9 k1, k2, ..., kn. Read the positive integers n and s,

k1 + 2 x k2 + 3 x k3 + ... + n x kn = s

Create a program that outputs how many rows of n numbers such as. However, the same number does not appear more than once in one "n sequence of numbers".



Input

The input consists of multiple datasets. For each dataset, n (1 ≤ n ≤ 10) and s (0 ≤ s ≤ 10,000) are given on one line, separated by blanks.

The number of datasets does not exceed 100.

Output

For each dataset, print the number of combinations in which the sum of n integers is s on one line.

Example

Input

3 10
3 1


Output

8
0
"""

def count_valid_combinations(n: int, s: int) -> int:
    """
    Counts the number of valid combinations of n numbers (each from 0 to 9) such that:
    k1 + 2 * k2 + 3 * k3 + ... + n * kn = s
    and no number appears more than once in the sequence.

    Parameters:
    n (int): The number of integers in the sequence.
    s (int): The target sum.

    Returns:
    int: The number of valid combinations.
    """
    from collections import defaultdict, Counter

    # Initialize the dynamic programming table
    dp = [defaultdict(Counter) for _ in range(11)]
    dp[0][0][0] = 1

    # Fill the dynamic programming table
    for i in range(1, 11):
        for (used, counter) in dp[i - 1].items():
            for j in filter(lambda x: used & 2 ** x == 0, range(10)):
                for (total, count) in counter.items():
                    dp[i][used | 2 ** j][total + j * i] += count

    # Calculate the result for the given n and s
    return sum((v for counter in dp[n].values() for (k, v) in counter.items() if k == s))