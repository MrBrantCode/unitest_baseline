"""
QUESTION:
A permutation of length $n$ is an array $p=[p_1,p_2,\dots,p_n]$, which contains every integer from $1$ to $n$ (inclusive) and, moreover, each number appears exactly once. For example, $p=[3,1,4,2,5]$ is a permutation of length $5$.

For a given number $n$ ($n \ge 2$), find a permutation $p$ in which absolute difference (that is, the absolute value of difference) of any two neighboring (adjacent) elements is between $2$ and $4$, inclusive. Formally, find such permutation $p$ that $2 \le |p_i - p_{i+1}| \le 4$ for each $i$ ($1 \le i < n$).

Print any such permutation for the given integer $n$ or determine that it does not exist.


-----Input-----

The first line contains an integer $t$ ($1 \le t \le 100$) — the number of test cases in the input. Then $t$ test cases follow.

Each test case is described by a single line containing an integer $n$ ($2 \le n \le 1000$).


-----Output-----

Print $t$ lines. Print a permutation that meets the given requirements. If there are several such permutations, then print any of them. If no such permutation exists, print -1.


-----Example-----
Input
6
10
2
4
6
7
13

Output
9 6 10 8 4 7 3 1 5 2 
-1
3 1 4 2 
5 3 6 2 4 1 
5 1 3 6 2 4 7 
13 9 7 11 8 4 1 3 5 2 6 10 12
"""

def find_permutations_with_constraints(t, n_list):
    """
    Finds permutations of length n for each test case where the absolute difference
    between any two neighboring elements is between 2 and 4, inclusive.

    Parameters:
    t (int): The number of test cases.
    n_list (list of int): A list of integers where each integer represents the length of the permutation to be found.

    Returns:
    list of list of int: A list where each element is either a permutation that meets the criteria or -1 if no such permutation exists.
    """
    results = []
    for n in n_list:
        if n < 4:
            results.append([-1])
        else:
            permutation = []
            for i in range(n - (1 - n % 2), 0, -2):
                permutation.append(i)
            permutation.append(4)
            for j in range(2, n + 1, 2):
                if j == 4:
                    continue
                permutation.append(j)
            results.append(permutation)
    return results