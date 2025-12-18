"""
QUESTION:
Given an integer array and a non-negative integer k, count all distinct pairs with difference equal to k, i.e., A[ i ] - A[ j ] = k
 
Example 1:
Input: array = {1, 5, 4, 1, 2}, k = 0
Output: 1
Explanation: There is only one pair (1, 1)
whose difference equal to 0.
Example 2;
Input: array = {1, 5, 3}, k = 2
Output: 2
Explanation: There are two pairs (5, 3) and 
(1, 3) whose difference equal to 2.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function TotalPairs() which takes array and k as input parameter and returns count of all distinct pairs.
 
Expected Time Complexity: O(Max(A_{i}))
Expected Space Complexity: O(Max(A_{i}))
 
Constraints:
0 <= length of array, k <= 100000
1 <= elements of array <= 100000
"""

def count_distinct_pairs_with_difference(nums, k):
    total = 0
    d = set()
    r = []
    
    for n in nums:
        if n - k in d:
            r.append([n - k, n])
            if k == 0:
                d.add(n)
                continue
        if n + k in d:
            r.append([n + k, n])
        d.add(n)
    
    di = dict()
    for x in r:
        sum_pair = x[0] + x[1]
        if sum_pair not in di:
            total += 1
            di[sum_pair] = 1
    
    return total