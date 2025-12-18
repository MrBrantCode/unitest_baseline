"""
QUESTION:
Range Minimum Query is a well-known problem: given an array of distinct integers with size $n=2^k$ and $m$ queries, find the minimum element on subsegment $[L_i,R_i]$.

One of the most efficient and famous solutions to this problem is a segment tree. A segment tree is a full binary tree with $2\cdot n-1$ nodes where the leaves contain the values of the original array and each non-leaf node contains the minimum value of its entire subtree.

Usually, a segment tree is represented as an array of integers with $2\cdot n-1$ elements. The left child of the $i^{\mbox{th}}$ node is in the $(2\cdot i+1)^{th}$ cell, and the right child is in the $(2\cdot i+2)^{th}$ cell. For example, $A=[1,1,3,1,2,3,4]$ represents the following segment tree where the first number in a node describes the array index, $\boldsymbol{i}$, in $\mbox{A}$ and the second number denotes the value stored at index $\boldsymbol{i}$ (which corresponds to the minimum value in that node's subtree):

You've just used $n$ distinct integers to construct your first segment tree and saved it as an array, $\mbox{A}$, of $2\cdot n-1$ values. Unfortunately, some evil guy came and either shuffled or altered the elements in your array. Can you use the altered data to restore the original array? If no, print NO on a new line; otherwise, print two lines where the first line contains the word YES and the second line contains $2\cdot n-1$ space-separated integers denoting the array's original values. If there are several possible original arrays, print the lexicographically smallest one.

Input Format

The first line contains a single integer, $n$, denoting the size of the array. 

The second line contains $2\cdot n-1$ space-separated integers denoting the shuffled values of the segment tree.

Constraints

$1\leq n\leq2^{18}$
$n$ is a power of two.
Each value in the segment tree is between $-10^9$ and $\mathbf{10^{9}}$.

Output Format

Print NO if this array could not be constructed by shuffling some segment tree. Otherwise, print YES on the first line, and $2\cdot n-1$ space-separated integers describing the respective values of the original array on the second line. If there are several possible answers, print the lexicographically smallest one.

Sample Input 0

4
3 1 3 1 2 4 1

Sample Output 0

YES
1 1 3 1 2 3 4 

Explanation 0 

This is the same segment tree shown in the Problem Statement above.

Sample Input 1

2
1 1 1

Sample Output 1

NO 

Explanation 1 

A segment tree with three nodes would consist of a root, a left child, and a right child. Because all three numbers in this array are the same and the leaves of the segment tree must be $n$ distinct integers, it's not possible to reconstruct the original array.
"""

import sys
from bisect import bisect_right

def restore_segment_tree(n, shuffled_values):
    nl = 0
    x = n
    while x:
        nl += 1
        x >>= 1
    
    occ = {}
    for e in shuffled_values:
        if e not in occ:
            occ[e] = 0
        occ[e] += 1
    
    cnt_occ = {}
    for v in occ.values():
        if v not in cnt_occ:
            cnt_occ[v] = 0
        cnt_occ[v] += 1
    
    for i in range(1, nl):
        if i not in cnt_occ or cnt_occ[i] != 1 << (nl - 1 - i):
            return "NO", []
    
    ah = [[] for _ in range(nl + 2)]
    for i, v in occ.items():
        ah[v].append(i)
    
    sofar = ah[nl]
    res = list(sofar)
    
    for i in range(1, nl):
        sofar = z(sofar, ah[nl - i])
        res += sofar
    
    return "YES", res

def z(a, b):
    B = sorted(b)
    r = []
    for i in range(len(a)):
        ind = bisect_right(B, a[i])
        r += [a[i], B[ind]]
        del B[ind]
    return r