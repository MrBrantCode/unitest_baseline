"""
QUESTION:
N problems have been chosen by the judges, now it's time to assign scores to them!

Problem i must get an integer score A_i between 1 and N, inclusive. The problems have already been sorted by difficulty: A_1 \le A_2 \le \ldots \le A_N must hold. Different problems can have the same score, though.

Being an ICPC fan, you want contestants who solve more problems to be ranked higher. That's why, for any k (1 \le k \le N-1), you want the sum of scores of any k problems to be strictly less than the sum of scores of any k+1 problems.

How many ways to assign scores do you have? Find this number modulo the given prime M.

Constraints

* 2 \leq N \leq 5000
* 9 \times 10^8 < M < 10^9
* M is a prime.
* All input values are integers.

Input

Input is given from Standard Input in the following format:


N M


Output

Print the number of ways to assign scores to the problems, modulo M.

Examples

Input

2 998244353


Output

3


Input

3 998244353


Output

7


Input

6 966666661


Output

66


Input

96 925309799


Output

83779
"""

def count_score_assignments(N: int, M: int) -> int:
    """
    Calculate the number of ways to assign scores to N problems such that:
    - Each problem i gets an integer score A_i between 1 and N, inclusive.
    - The problems are sorted by difficulty: A_1 <= A_2 <= ... <= A_N.
    - For any k (1 <= k <= N-1), the sum of scores of any k problems is strictly less than the sum of scores of any k+1 problems.
    
    The result is returned modulo M.

    Parameters:
    - N (int): The number of problems.
    - M (int): The prime modulo.

    Returns:
    - int: The number of ways to assign scores modulo M.
    """
    A = list(range(1, N // 2 + 1)) * 2
    if N & 1:
        A += [(N + 1) // 2]
    d = [1] + [0] * (N + N)
    for x in A:
        for i in range(N + 1):
            d[i] %= M
            d[i + x] += d[i]
    return sum(d[:N]) % M