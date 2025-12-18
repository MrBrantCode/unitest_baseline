"""
QUESTION:
Given an array A[ ] and its size N your task is to complete two functions  a constructST  function which builds the segment tree  and a function RMQ which finds range minimum query in a range [a,b] of the given array.
Input:
The task is to complete two functions constructST and RMQ.
The constructST function builds the segment tree and takes two arguments the array A[ ] and the size of the array N.
It returns a pointer to the first element of the segment tree array.
The RMQ function takes 4 arguments the first being the segment tree st constructed, second being the size N and then third and forth arguments are the range of query a and b. The function RMQ returns the min of the elements in the array from index range a and b. There are multiple test cases. For each test case, this method will be called individually.
Output:
The function RMQ should return the min element in the array from range a to b.
Example:
Input (To be used only for expected output) 
1
4
1 2 3 4
2
0 2 2 3
Output
1 3
Explanation
1. For query 1 ie 0 2 the element in this range are 1 2 3 
   and the min element is 1. 
2. For query 2 ie 2 3 the element in this range are 3 4 
   and the min element is 3.
Constraints:
1<=T<=100
1<=N<=10^3+1
1<=A[i]<=10^9
1<=Q(no of queries)<=10000
0<=a<=b
"""

import sys

def segment_tree_min_query(arr, queries):
    n = len(arr)
    st = [sys.maxsize] * (4 * n)

    def build(node, l, r):
        if l == r:
            st[node] = arr[l]
        else:
            m = (l + r) // 2
            build(2 * node + 1, l, m)
            build(2 * node + 2, m + 1, r)
            st[node] = min(st[2 * node + 1], st[2 * node + 2])
    
    build(0, 0, n - 1)
    
    def mini(node, l, r, qs, qe):
        if qs > r or qe < l:
            return sys.maxsize
        if qs <= l and qe >= r:
            return st[node]
        m = (l + r) // 2
        return min(mini(2 * node + 1, l, m, qs, qe), mini(2 * node + 2, m + 1, r, qs, qe))
    
    results = []
    for qs, qe in queries:
        results.append(mini(0, 0, n - 1, qs, qe))
    
    return results