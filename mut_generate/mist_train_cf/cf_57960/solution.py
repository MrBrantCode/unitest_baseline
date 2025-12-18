"""
QUESTION:
Determine if an even-length integer array can be rearranged such that every pair of elements at indices 2*i and 2*i+1 satisfies arr[2 * i + 1] = 2 * arr[2 * i]. Given function name: canReorderDoubled(arr). The array length is even, and all elements are within the range -10^5 to 10^5.
"""

from collections import Counter
from queue import PriorityQueue

def canReorderDoubled(arr):
    counter = Counter(arr)
    queue = PriorityQueue()
    for num in counter:
        queue.put((abs(num), num)) 
    while not queue.empty():
        num = queue.get()[1] 
        if not counter[num]: 
            continue
        if counter[2*num] < counter[num]: 
            return False
        counter[2*num] = counter[2*num] - counter[num]
        counter[num] = 0
    return True