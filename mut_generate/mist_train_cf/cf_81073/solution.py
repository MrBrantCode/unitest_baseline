"""
QUESTION:
Given two integers `low` and `high`, implement the function `stepNum(low, high)` to return a dictionary of all Stepping Numbers in the range `[low, high]` inclusive, where a Stepping Number is an integer with all adjacent digits having an absolute difference of exactly `1`. The dictionary should have Stepping Numbers as keys and the sum of their digits as values. The function should handle the constraints `0 <= low <= high <= 2 * 10^9`.
"""

import collections

def stepNum(low, high):
    result = dict()
    queue = collections.deque()
    for i in range(1, 10):
        queue.append(i)

    if low == 0:
        result[0] = 0

    while queue:
        num = queue.popleft()

        if low <= num <= high:
            result[num] = sum([int(i) for i in str(num)])

        last_digit = num % 10
        numA = num * 10 + (last_digit-1)
        numB = num * 10 + (last_digit+1)

        if last_digit == 0 and numB <= high:
            queue.append(numB)
        elif last_digit == 9 and numA <= high:
            queue.append(numA)
        else:
            if numA <= high:
                queue.append(numA)
            if numB <= high:
                queue.append(numB)
        
    return result