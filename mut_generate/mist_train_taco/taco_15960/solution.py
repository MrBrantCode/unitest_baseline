"""
QUESTION:
Consider the following $4 \times 4$ pattern:
1  2  4  7
3  5  8 11
6  9 12 14
10 13 15 16

You are given an integer $N$. Print the $N \times N$ pattern of the same kind (containing integers $1$ through $N^2$).

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

-----Output-----
For each test case, print $N$ lines; each of them should contain $N$ space-separated integers.

-----Constraints-----
- $1 \le T \le 10$
- $1 \le N \le 100$

-----Subtasks-----
Subtask #1 (100 points): Original constraints

-----Example Input-----
1
4

-----Example Output-----
1 2 4 7
3 5 8 11
6 9 12 14
10 13 15 16

-----Explanation-----
"""

def generate_pattern(N):
    """
    Generates an N x N pattern of integers from 1 to N^2 in a specific order.

    Parameters:
    - N (int): The size of the pattern (N x N).

    Returns:
    - list: A 2D list representing the N x N pattern.
    """
    arr = [[0] * N for _ in range(N)]
    c = 1
    
    # Fill the pattern diagonally
    for j in range(N):
        for k in range(j + 1):
            arr[k][j - k] = c
            c += 1
    
    for j in range(1, N):
        for k in range(N - j):
            arr[j + k][N - k - 1] = c
            c += 1
    
    return arr