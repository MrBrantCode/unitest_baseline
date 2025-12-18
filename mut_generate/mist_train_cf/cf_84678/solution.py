"""
QUESTION:
Write a function `sequentialDigits` that takes two integers `low` and `high` as input where `10 <= low <= high <= 10^18`. The function should return a sorted list of all integers in the range `[low, high]` inclusive that have sequential digits, along with the count of such integers. The function should have a time complexity of O(n log n), where n is the number of integers in the range `[low, high]`.
"""

def sequentialDigits(low, high):
    queue = [i for i in range(1,10)]
    res = []
    while queue:
        i = queue.pop(0)
        if low <= i <= high:
            res.append(i)
        if i % 10 + 1 < 10:
            queue.append(i * 10 + i % 10 + 1)
    res.sort()
    return res, len(res)