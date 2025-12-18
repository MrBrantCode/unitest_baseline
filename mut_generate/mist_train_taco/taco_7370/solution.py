"""
QUESTION:
You are given a sequence $A_1, A_2, \ldots, A_N$. Calculate the number of ways to remove a non-empty contiguous subsequence from it such that the resulting sequence is non-empty and strictly increasing.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

-----Output-----
For each test case, print a single line containing one integer ― the number of ways.

-----Constraints-----
- $1 \le T \le 10$
- $1 \le N \le 10^5$
- $|A_i| \le 10^9$ for each valid $i$

-----Subtasks-----
Subtask #1 (40 points): $N \le 1,000$
Subtask #2 (60 points): original constraints

-----Example Input-----
2
3
1 1 2
4
2 4 3 5

-----Example Output-----
4
7
"""

def count_ways_to_remove_subsequence(test_cases):
    results = []
    
    for case in test_cases:
        N, A = case
        prefix = [False] * N
        suffix = [False] * N
        
        # Determine prefix increasing sequence
        prefix[0] = True
        for i in range(1, N):
            if A[i] > A[i - 1]:
                prefix[i] = True
            else:
                break
        
        # Determine suffix increasing sequence
        suffix[N - 1] = True
        for i in range(N - 2, -1, -1):
            if A[i] < A[i + 1]:
                suffix[i] = True
            else:
                break
        
        ans = 0
        if prefix.count(True) == N:
            ans = N * (N - 1) / 2 + (N - 1)
        else:
            for i in range(N):
                if prefix[i]:
                    low = i
                    high = N
                    while high - low > 1:
                        mid = (low + high) // 2
                        if suffix[mid] and A[i] < A[mid]:
                            high = mid
                        else:
                            low = mid
                    ans += N - high
                else:
                    break
            ans += suffix.count(True)
            ans += prefix.count(True)
        
        results.append(int(ans))
    
    return results