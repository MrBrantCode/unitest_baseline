"""
QUESTION:
Write a function `shortestSubarray(A, K)` that returns the length of the shortest, non-empty, contiguous subarray of `A` with sum at least `K`, along with its starting and ending indices. If there is no non-empty subarray with sum at least `K`, return `-1`.

Restrictions:
- `1 <= A.length <= 50000`
- `-10^5 <= A[i] <= 10^5`
- `1 <= K <= 10^9`
"""

from collections import deque

def shortestSubarray(A, K):
    B = [0]
    for a in A:
        B.append(B[-1] + a)

    res = float('inf')
    idx = [-1, -1]
    queue = deque()

    for i, b in enumerate(B):
        while queue and b <= B[queue[-1]]:
            queue.pop()

        while queue and b - B[queue[0]] >= K:
            res = min(res, i - B[queue[0]])
            if res == i - queue[0]:
                idx = [queue[0], i - 1]
            queue.popleft()

        queue.append(i)

    return [res, idx[0], idx[1]] if res != float('inf') else -1