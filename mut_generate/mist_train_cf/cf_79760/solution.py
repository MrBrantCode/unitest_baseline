"""
QUESTION:
Given an array of integers `arr`, an integer `k`, and a limit `m`, find the least number of unique integers after removing exactly `k` elements. However, you are not allowed to remove more than `m` instances of the same number. Implement a function `findLeastNumOfUniqueInts(arr, k, m)` that returns the least number of unique integers after removal, with the constraints that `1 <= arr.length <= 10^5`, `1 <= arr[i] <= 10^9`, `0 <= k <= arr.length`, and `1 <= m <= arr.length`.
"""

import heapq
from collections import Counter

def findLeastNumOfUniqueInts(arr, k, m):
    count = Counter(arr)
    heap = [(freq, num) for num, freq in count.items()]
    heapq.heapify(heap)

    while k > 0 and heap:
        freq, num = heapq.heappop(heap)

        if freq <= m:
            if freq <= k:
                k -= freq
            else:
                heapq.heappush(heap, (freq - k, num))
                k = 0
        else:
            to_remove = min(k, m)
            k -= to_remove
            freq -= to_remove

            if freq > 0:
                heapq.heappush(heap, (freq, num))

    while k > 0:
        freq, num = count.most_common(1)[0]
        to_remove = min(k, freq)
        k -= to_remove
        del count[num]

    return len(heap)