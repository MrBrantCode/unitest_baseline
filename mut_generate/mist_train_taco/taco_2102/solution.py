"""
QUESTION:
Permutation p is an ordered set of integers p_1,   p_2,   ...,   p_{n}, consisting of n distinct positive integers not larger than n. We'll denote as n the length of permutation p_1,   p_2,   ...,   p_{n}.

Your task is to find such permutation p of length n, that the group of numbers |p_1 - p_2|, |p_2 - p_3|, ..., |p_{n} - 1 - p_{n}| has exactly k distinct elements.


-----Input-----

The single line of the input contains two space-separated positive integers n, k (1 ≤ k < n ≤ 10^5).


-----Output-----

Print n integers forming the permutation. If there are multiple answers, print any of them.


-----Examples-----
Input
3 2

Output
1 3 2

Input
3 1

Output
1 2 3

Input
5 2

Output
1 3 2 4 5



-----Note-----

By |x| we denote the absolute value of number x.
"""

def generate_permutation(n: int, k: int) -> list[int]:
    """
    Generates a permutation of length n such that the group of numbers |p_1 - p_2|, |p_2 - p_3|, ..., |p_{n-1} - p_{n}|
    has exactly k distinct elements.

    Parameters:
    - n (int): The length of the permutation.
    - k (int): The number of distinct elements in the group of differences.

    Returns:
    - list[int]: A list of integers representing the permutation.
    """
    a = [n - i // 2 if i & 1 else i // 2 + 1 for i in range(n)]
    a[k:] = sorted(a[k:])[::-1] if a[k - 1] > n / 2 else sorted(a[k:])
    return a