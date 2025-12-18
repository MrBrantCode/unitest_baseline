"""
QUESTION:
Read problems statements in mandarin chinese, russian and vietnamese as well. 

Though our Head Chef retired from sport programming long back, but that did not affect his passion to contribute to the programming community. He still remains engaged by creating new problems and passing it on to the online judges. Last Night, he thought of a following problem for which he could not figure out a solution. You being his friend from the older days of programming decide to help him.

Find the number of non-empty subsequences in the given list of N integers such that the product of the values in the subsequences does not exceed K

------ Input ------ 

First line of the input will contain two space separated integers N and K. Next and last line of the input contains N space separated integers

------ Output ------ 

Print the answer to the given test case in a separate line.

------ Constraints ------ 

$1 ≤ N ≤ 30$
$1 ≤ K, A_{i} ≤ 10^{18}$

------ Subtasks ------ 

Subtask #1 : (30 points)

$1 ≤ N ≤ 10$

Subtask #2 : (70 points) 

$1 ≤ N ≤ 30$

----- Sample Input 1 ------ 
3 4

1 2 3
----- Sample Output 1 ------ 
5
----- explanation 1 ------ 

For the given sample case, there are 7 non-empty subsequences out of which 2 have their product > 4. Those include {2, 3} and {1, 2, 3}. Hence, the answer is 7 - 2 = 5.
"""

import bisect

def count_valid_subsequences(N, K, arr):
    def create_subsets(arr, k):
        subset = []
        l = len(arr)
        val = 2 ** l
        for i in range(val):
            s = 1
            for j in range(l):
                if i & 1 << j:
                    s *= arr[j]
            if s <= k:
                subset.append(s)
        subset.sort()
        return subset

    b = arr[:N // 2]
    c = arr[N // 2:]
    subset1 = create_subsets(b, K)
    subset2 = create_subsets(c, K)
    
    ans = 0
    for i in subset1:
        ans += bisect.bisect_right(subset2, K // i)
    
    return ans - 1