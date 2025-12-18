"""
QUESTION:
A flea is sitting at one of the n hassocks, arranged in a circle, at the moment. After minute number k the flea jumps through k - 1 hassoсks (clockwise). For example, after the first minute the flea jumps to the neighboring hassock. You should answer: will the flea visit all the hassocks or not. We assume that flea has infinitely much time for this jumping.

Input

The only line contains single integer: 1 ≤ n ≤ 1000 — number of hassocks.

Output

Output "YES" if all the hassocks will be visited and "NO" otherwise.

Examples

Input

1


Output

YES


Input

3


Output

NO
"""

def will_flea_visit_all_hassocks(n: int) -> str:
    visited = [False] * n
    k = 0
    for i in range(n ** 2 + 1):
        k += i + 1
        visited[k % n] = True
    
    for i in visited:
        if not i:
            return 'NO'
    
    return 'YES'