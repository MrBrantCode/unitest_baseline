"""
QUESTION:
You are given two positive integers $N$ and $K$, where $K \le N$. Find a sequence $A_1, A_2, \ldots, A_N$ such that:
- for each valid $i$, $A_i$ is either $i$ or $-i$
- there are exactly $K$ values of $i$ such that $1 \le i \le N$ and $A_1 + A_2 + \ldots + A_i > 0$
If there are multiple solutions, you may print any one of them. It can be proved that at least one solution always exists.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N$ and $K$.

-----Output-----
For each test case, print a single line containing $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

-----Constraints-----
- $1 \le T \le 1,000$
- $1 \le K \le N \le 1,000$

-----Subtasks-----
Subtask #1 (10 points): $N \le 10$
Subtask #2 (90 points): original constraints

-----Example Input-----
1
3 3

-----Example Output-----
1 2 3
"""

def generate_sequence(N: int, K: int) -> list[int]:
    """
    Generates a sequence of length N such that there are exactly K values of i
    for which the prefix sum A_1 + A_2 + ... + A_i is positive.

    Parameters:
    - N (int): The length of the sequence.
    - K (int): The number of positive prefix sums required.

    Returns:
    - list[int]: A list of integers representing the sequence.
    """
    cnt = N // 2
    diff = N - K
    sequence = []
    
    if K > cnt:
        for i in range(1, N + 1):
            if diff > 0 and i % 2 == 1:
                diff -= 1
                sequence.append(-i)
            else:
                sequence.append(i)
    else:
        for i in range(1, N + 1):
            if K > 0 and i % 2 == 0:
                K -= 1
                sequence.append(i)
            else:
                sequence.append(-i)
    
    return sequence