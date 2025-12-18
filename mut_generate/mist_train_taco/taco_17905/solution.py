"""
QUESTION:
You are given an integer sequence $A_1, A_2, \ldots, A_N$ and an integer $X$. Consider a $N \times N$ matrix $B$, where $B_{i,j} = A_i + A_j$ for each valid $i$ and $j$.
You need to find the number of square submatrices of $B$ such that the sum of their elements is $X$. Formally, find the number of quartets $(x_1, y_1, x_2, y_2)$ such that $1 \le x_1 \le x_2 \le N$, $1 \le y_1 \le y_2 \le N$, $x_2-x_1 = y_2-y_1$ and $\sum_{i=x_1}^{x_2}\sum_{j=y_1}^{y_2} B_{i,j} = X$.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $X$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

-----Output-----
For each test case, print a single line containing one integer ― the number of square submatrices with sum $X$.

-----Constraints-----
- $1 \le T \le 100$
- $1 \le X \le 10^6$
- $1 \le N \le 10^5$
- $1 \le A_i \le 10^6$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^6$

-----Subtasks-----
Subtask #1 (50 points): the sum of $N$ over all test cases does not exceed $1,000$
Subtask #2 (50 points): original constraints

-----Example Input-----
2
5 36
1 2 3 1 12
4 54
3 3 3 3

-----Example Output-----
6
4
"""

def count_square_submatrices_with_sum(N, X, A):
    # Precompute prefix sums
    pre = [0] * (N + 1)
    sum = 0
    for i in range(1, N + 1):
        sum += A[i - 1]
        pre[i] = sum
    
    # Find all factors of X
    factors = []
    i = 1
    while i * i <= X:
        if X % i == 0:
            factors.append(i)
            if i * i != X:
                factors.append(X // i)
        i += 1
    
    ans = 0
    for a in factors:
        if a > N:
            continue
        z = X // a
        dict = {}
        
        # First pass: count occurrences of each possible sum
        for j in range(a, N + 1):
            s = pre[j] - pre[j - a]
            if s > z:
                continue
            if s in dict:
                dict[s] += 1
            else:
                dict[s] = 1
        
        # Second pass: count valid submatrices
        for j in range(a, N + 1):
            s = pre[j] - pre[j - a]
            if s > z:
                continue
            if z - s in dict:
                ans += dict[z - s]
        
        # Clear the dictionary for the next factor
        for j in range(a, N + 1):
            s = pre[j] - pre[j - a]
            if s > z:
                continue
            dict[s] = 0
    
    return ans