"""
QUESTION:
You are given an integer array representing the number of dresses in each washing machine from left to right on a line. Your task is to find the minimum number of moves to make all the washing machines have the same number of dresses. A move consists of choosing any number of washing machines and passing one dress of each machine to one of its adjacent machines at the same time. However, each washing machine can only pass a dress to an adjacent machine if it has more than one dress. If it is not possible to make all the washing machines have the same number of dresses, return -1.

The function name is `findMinMoves`. The input is an integer array `machines` of length `n`, where `1 ≤ n ≤ 10000` and `0 ≤ machines[i] ≤ 1e5`.
"""

def findMinMoves(machines):
    """
    :type machines: List[int]
    :rtype: int
    """
    total = sum(machines)
    n = len(machines)
    if total % n:
        return -1

    target = total / n
    right = [0] * n
    right[-1] = machines[-1] - target
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] + machines[i] - target

    ans = max(right)
    left = 0
    for i in range(n):
        ans = max(ans, abs(left), right[i])
        left += machines[i] - target

    return ans