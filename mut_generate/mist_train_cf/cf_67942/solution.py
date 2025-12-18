"""
QUESTION:
Write a function `divide_chocolate(sweetness, K, preference)` that takes in three parameters: an array `sweetness` representing the sweetness of each chunk, an integer `K` representing the number of cuts, and an array `preference` representing the additional sweetness perceived in each chunk. 

The function should return the maximum total sweetness of the piece that can be obtained by cutting the chocolate bar optimally. The total sweetness of each piece is the sum of the sweetness of its chunks plus the additional sweetness perceived in its chunks.

The constraints are that `0 <= K < min(sweetness.length, preference.length) <= 10^4` and `1 <= sweetness[i], preference[i] <= 10^5`.
"""

def divide_chocolate(sweetness, K, preference):
    preferred_sweetness = [s+p for s, p in zip(sweetness, preference)]
    low, high = min(preferred_sweetness), sum(preferred_sweetness)
    while low < high:
        mid = (low + high + 1) // 2
        chunks = cuts = 0
        for s in preferred_sweetness:
            chunks += s
            if chunks >= mid:
                chunks = 0
                cuts += 1
                if cuts > K:
                    break
        if cuts > K:
            low = mid
        else:
            high = mid - 1
    return high