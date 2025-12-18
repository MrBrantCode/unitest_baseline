"""
QUESTION:
Define a function `unique_subarrays` that takes a list of integers and an integer `k` as input. The function should return the total number of unique subarrays within the sorted list that have no duplicates and the difference between the maximum and minimum elements is less than or equal to `k`. The input list can contain up to 1000 elements, each integer is between -10^9 and 10^9, and `k` is between 1 and 10^6.
"""

def unique_subarrays(lst, k):
    lst.sort()
    i, j, ans = 0, 0, 0
    seen = set()
    while i < len(lst):
        if lst[i] in seen:
            i += 1
            continue
        while j < len(lst) and lst[j] - lst[i] <= k:
            j += 1
        ans += j - i - 1
        seen.add(lst[i])
        i += 1
    return ans