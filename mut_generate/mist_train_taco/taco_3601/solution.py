"""
QUESTION:
# Task
 Sorting is one of the most basic computational devices used in Computer Science. 
 
 Given a sequence (length ≤ 1000) of 3 different key values (7, 8, 9), your task is to find the minimum number of exchange operations necessary to make the sequence sorted. 

 One operation is the switching of 2 key values in the sequence.

# Example

 For `sequence = [7, 7, 8, 8, 9, 9]`, the result should be `0`.
 
 It's already a sorted sequence.

 For `sequence = [9, 7, 8, 8, 9, 7]`, the result should be `1`.
 
 We can switching `sequence[0]` and `sequence[5]`.
 
 For `sequence = [8, 8, 7, 9, 9, 9, 8, 9, 7]`, the result should be `4`.
 
 We can:
```
 [8, 8, 7, 9, 9, 9, 8, 9, 7] 
 switching sequence[0] and sequence[3]
 --> [9, 8, 7, 8, 9, 9, 8, 9, 7]
 switching sequence[0] and sequence[8]
 --> [7, 8, 7, 8, 9, 9, 8, 9, 9]
 switching sequence[1] and sequence[2]
 --> [7, 7, 8, 8, 9, 9, 8, 9, 9]
 switching sequence[5] and sequence[7]
 --> [7, 7, 8, 8, 8, 9, 9, 9, 9] 
```
So `4` is the minimum number of operations for the sequence to become sorted.

# Input/Output


 - `[input]` integer array `sequence`

  The Sequence.


 - `[output]` an integer

  the minimum number of operations.
"""

from collections import Counter

def minimum_exchange_operations(sequence):
    swaps = 0
    cnt = Counter()
    
    for a, b in zip(sequence, sorted(sequence)):
        if cnt[b, a] > 0:
            cnt[b, a] -= 1
            swaps += 1
        elif a != b:
            cnt[a, b] += 1
    
    return swaps + sum(cnt.values()) // 3 * 2