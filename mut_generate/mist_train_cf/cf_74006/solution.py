"""
QUESTION:
Given a numerical array `A` of length 1-12 composed of non-negative integers up to 1e9, write a function `numSquarefulPerms(A)` that returns the number of distinct permutations of `A` where the sum of every pair of contiguous elements is a perfect square.
"""

import collections

def checkPerfect(n):
    return int(n**0.5)**2 == n

def numSquarefulPerms(A):
    count = collections.Counter(A)
    pairs = collections.defaultdict(list)
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if checkPerfect(A[i] + A[j]):
                pairs[A[i]].append(A[j])
                pairs[A[j]].append(A[i])
                
    result = set()
    def dfs(path):
        if len(path) == len(A):
            result.add(tuple(path))
            return
        for num in count:
            if count[num]:
                if not path or checkPerfect(path[-1] + num):
                    count[num] -= 1
                    dfs(path + [num])
                    count[num] += 1
                    
    dfs([])
    return len(result)