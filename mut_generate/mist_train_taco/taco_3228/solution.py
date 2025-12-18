"""
QUESTION:
Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.








 
Example 1:
Input: A = [3,1,3,6]
Output: false

Example 2:
Input: A = [2,1,2,6]
Output: false

Example 3:
Input: A = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].

Example 4:
Input: A = [1,2,4,16,8,4]
Output: false

 
Constraints:

0 <= A.length <= 3 * 104
A.length is even.
-105 <= A[i] <= 105
"""

from collections import Counter
from typing import List

def can_reorder_doubled(A: List[int]) -> bool:
    cache = Counter(A)
    c_list = sorted(list(cache), key=abs)
    for x in c_list:
        if cache[x] > cache[2 * x]:
            return False
        cache[2 * x] -= cache[x]
    return True