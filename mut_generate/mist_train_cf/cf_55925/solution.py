"""
QUESTION:
You are given an array `sweetness` representing the sweetness of each chunk of a chocolate bar, an integer `K` representing the number of cuts to make, an array `preference` representing the additional sweetness you perceive in each chunk, and an array `noCut` where `noCut[i]` is 1 if you cannot cut at chunk `i` and 0 otherwise. 

You want to divide the chocolate bar into `K+1` pieces using `K` cuts, each piece consisting of some consecutive chunks, and find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally. The function should be named `maxSweetness` and it should take `sweetness`, `K`, `preference`, and `noCut` as input parameters. 

The function should return the maximum total sweetness of the piece you can get. The constraints are `0 <= K < min(sweetness.length, preference.length, noCut.length) <= 10^4`, `1 <= sweetness[i], preference[i] <= 10^5`, and `0 <= noCut[i] <= 1`.
"""

def maxSweetness(sweetness, K, preference, noCut):
    chunks = []
    i = 0

    while i < len(sweetness):
        total = sweetness[i] + preference[i]
        i += 1

        while i < len(sweetness) and noCut[i-1] == 1:
            total += sweetness[i] + preference[i]
            i += 1

        chunks.append(total)

    l, r = 1, sum(chunks) // (K+1)
    answer = 0

    while l <= r:
        mid = l + (r - l) // 2
        pieces = cuts = 0
        min_piece = float('inf')

        for i in range(len(chunks)):
            pieces += chunks[i]
            if pieces >= mid:
                min_piece = min(min_piece, pieces)
                pieces = 0
                cuts += 1

        if cuts > K:
            answer = max(answer, min_piece)
            l = mid + 1
        else:
            r = mid - 1

    return answer