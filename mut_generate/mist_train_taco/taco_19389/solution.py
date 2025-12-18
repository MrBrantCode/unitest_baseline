"""
QUESTION:
Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.

Return the size of the largest connected component in the graph.
 



Example 1:
Input: [4,6,15,35]
Output: 4



Example 2:
Input: [20,50,9,63]
Output: 2



Example 3:
Input: [2,3,6,7,4,12,21,39]
Output: 8


Note:

1 <= A.length <= 20000
1 <= A[i] <= 100000
"""

from collections import defaultdict

# Precompute prime factors for numbers up to 100000
MAXPRIME = 100001
isPrime = [0 for _ in range(MAXPRIME + 1)]
isPrime[0] = -1
isPrime[1] = -1
for i in range(2, MAXPRIME):
    if isPrime[i] == 0:
        for multiple in range(i * i, MAXPRIME + 1, i):
            if isPrime[multiple] == 0:
                isPrime[multiple] = i
        isPrime[i] = i

def largest_component_size(A):
    label = defaultdict(int)

    def findRoot(key):
        if label[key] > 0:
            label[key] = findRoot(label[key])
            return label[key]
        else:
            return key

    def mergeRoot(k1, k2):
        (r1, r2) = (findRoot(k1), findRoot(k2))
        if r1 != r2:
            (r1, r2) = (min(r1, r2), max(r1, r2))
            label[r1] += label[r2]
            label[r2] = r1
        return r1

    for x in A:
        root_id = 0
        prime_factors = set()
        while isPrime[x] != -1:
            p = isPrime[x]
            root_id = findRoot(p) if root_id == 0 else mergeRoot(root_id, p)
            x //= p
        label[root_id] -= 1

    return -min(label.values())