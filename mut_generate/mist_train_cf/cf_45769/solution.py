"""
QUESTION:
Given a list of distinct integers `arr` and an integer `k`, implement a function `getLoser` to determine the integer that loses a game where the first two elements of the array play rounds, the smaller integer wins and remains at the front, and the larger integer moves to the end of the array, until an integer loses `k` consecutive rounds. The function should return the losing integer. The array length is between 2 and 10^5, each integer in the array is between 1 and 10^6, and `k` is between 1 and 10^9.
"""

from collections import deque

def getLoser(arr, k):
    dq = deque([arr[0]])
    max_lost = arr[0]
    lose_count = 0
    for i in range(1, len(arr)):
        if arr[i] < dq[0]:
            lose_count += 1
            max_lost = max(max_lost, dq[0])
            dq.append(arr[i])
            if lose_count == k: 
                return max_lost
        else:
            lose_count = 1
            max_lost = dq[0]
            dq.append(dq.popleft())
            dq[0] = arr[i]
    return dq[0]