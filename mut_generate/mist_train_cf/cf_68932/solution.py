"""
QUESTION:
Write a function `minSetSize(arr)` that takes an array of integers as input, where the length of the array is between 1 and 10^5, inclusive, and each integer in the array is between 1 and 10^5, inclusive. The length of the array is divisible by 4. The function should return the minimum size of the set of integers that can be removed from the array so that at least three quarters of the integers in the array are removed.
"""

from collections import Counter
import operator

def minSetSize(arr):
    n = len(arr)
    freq = dict(Counter(arr))

    # sort frequencies in descending order
    freq = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)
    
    size = sum(v for k,v in freq)
    count = 0

    # reduce array size until it becomes less or equal to n/4
    for k, v in freq:
        if size > n//4:
            size -= v
            count += 1
        else:
            break
    return count