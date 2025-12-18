"""
QUESTION:
Construct a function named `movesToStamp` that takes two parameters: `stamp` and `target`, both of which are strings consisting of lowercase alphabets. The function should return an array of indices representing the left-most letter stamped at each round to stamp the `target` sequence using the `stamp` within `10 * target.length` moves. If it's impossible to stamp the sequence, return an empty array. The length of `stamp` is between 1 and `target.length` (inclusive), and the length of `target` is at most 1000.
"""

from collections import deque

def movesToStamp(stamp: str, target: str) -> list[int]:
    M, N = len(stamp), len(target)
    queue, done = deque(), [False] * N
    A = []
    for i in range(N - M + 1):
        made, todo = set(), deque()
        for j in range(M):
            if target[i+j] == stamp[j]: made.add(i+j)
            else: todo.append((i+j, stamp[j]))
        A.append((made, todo))

    ans = []
    while queue or any(not A[i][1] for i in range(N - M + 1) if not done[i]):
        queue = deque([i for i in range(N - M + 1) if not done[i] and not A[i][1]])
        for i in queue:
            ans.append(i)
            for b in A[i][0]: done[b] = True
    return ans[::-1] if all(done) else []