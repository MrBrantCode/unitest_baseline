"""
QUESTION:
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.
(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
Return the number of good subarrays of A.
 
Example 1:
Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

Example 2:
Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

 
Note:

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
"""

from collections import defaultdict
from typing import List

def count_good_subarrays(A: List[int], K: int) -> int:
    start_k = 0
    start = 0
    elem_dict = defaultdict(int)
    ans = 0
    
    for elem in A:
        elem_dict[elem] += 1
        
        if len(elem_dict) > K:
            del elem_dict[A[start_k]]
            start_k += 1
            start = start_k
        
        if len(elem_dict) == K:
            while elem_dict[A[start_k]] > 1:
                elem_dict[A[start_k]] -= 1
                start_k += 1
            ans = ans + start_k - start + 1
    
    return ans