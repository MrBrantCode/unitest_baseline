"""
QUESTION:
Suppose $a_1, a_2, \dots, a_n$ is a sorted integer sequence of length $n$ such that $a_1 \leq a_2 \leq \dots \leq a_n$.

For every $1 \leq i \leq n$, the prefix sum $s_i$ of the first $i$ terms $a_1, a_2, \dots, a_i$ is defined by $$ s_i = \sum_{k=1}^i a_k = a_1 + a_2 + \dots + a_i. $$

Now you are given the last $k$ terms of the prefix sums, which are $s_{n-k+1}, \dots, s_{n-1}, s_{n}$. Your task is to determine whether this is possible.

Formally, given $k$ integers $s_{n-k+1}, \dots, s_{n-1}, s_{n}$, the task is to check whether there is a sequence $a_1, a_2, \dots, a_n$ such that

$a_1 \leq a_2 \leq \dots \leq a_n$, and

$s_i = a_1 + a_2 + \dots + a_i$ for all $n-k+1 \leq i \leq n$.


-----Input-----

Each test contains multiple test cases. The first line contains an integer $t$ ($1 \leq t \leq 10^5$) — the number of test cases. The following lines contain the description of each test case.

The first line of each test case contains two integers $n$ ($1 \leq n \leq 10^5$) and $k$ ($1 \leq k \leq n$), indicating the length of the sequence $a$ and the number of terms of prefix sums, respectively.

The second line of each test case contains $k$ integers $s_{n-k+1}, \dots, s_{n-1}, s_{n}$ ($-10^9 \leq s_i \leq 10^9$ for every $n-k+1 \leq i \leq n$).

It is guaranteed that the sum of $n$ over all test cases does not exceed $10^5$.


-----Output-----

For each test case, output "YES" (without quotes) if it is possible and "NO" (without quotes) otherwise.

You can output "YES" and "NO" in any case (for example, strings "yEs", "yes" and "Yes" will be recognized as a positive response).


-----Examples-----

Input
4
5 5
1 2 3 4 5
7 4
-6 -5 -3 0
3 3
2 3 4
3 2
3 4
Output
Yes
Yes
No
No


-----Note-----

In the first test case, we have the only sequence $a = [1, 1, 1, 1, 1]$.

In the second test case, we can choose, for example, $a = [-3, -2, -1, 0, 1, 2, 3]$.

In the third test case, the prefix sums define the only sequence $a = [2, 1, 1]$, but it is not sorted.

In the fourth test case, it can be shown that there is no sequence with the given prefix sums.
"""

def is_possible_sequence(n, k, prefix_sums):
    """
    Determines whether it is possible to construct a sorted sequence a_1, a_2, ..., a_n
    such that the given prefix sums are valid.

    Parameters:
    n (int): The length of the sequence.
    k (int): The number of terms of prefix sums.
    prefix_sums (list of int): A list of the last k terms of the prefix sums.

    Returns:
    bool: True if it is possible to construct the sequence, False otherwise.
    """
    if k == 1:
        return True
    elif prefix_sums[1] - prefix_sums[0] < prefix_sums[0] / (n - k + 1):
        return False
    else:
        for i in range(1, k - 1):
            if prefix_sums[i] - prefix_sums[i - 1] > prefix_sums[i + 1] - prefix_sums[i]:
                return False
        return True