"""
QUESTION:
Implement a function `getKth` that takes three integers `lo`, `hi`, and `k` as input, where `1 <= lo < hi <= 1000` and `1 <= k <= hi - lo + 1`. The function should return the k-th integer in the range `[lo, hi]` sorted by the power value in ascending order. The power of an integer `x` is defined as the number of steps needed to transform `x` into `1` using the following steps: if `x` is even then `x = x / 2`, if `x` is odd then `x = 3 * x + 1`. If two or more integers have the same power value, sort them by ascending order.
"""

import heapq

def getKth(lo: int, hi: int, k: int) -> int:
    def power(x):
        count = 0
        while x != 1:
            if x % 2 == 0: x //= 2
            else: x = 3 * x + 1
            count += 1
        return count

    # Priority Queue to store (Power_value,x)
    pq = [(power(x), x) for x in range(lo, hi+1)]

    # Heapify the queue
    heapq.heapify(pq)

    while True:
        pow,val = heapq.heappop(pq)
        k -= 1
        if k == 0: return val