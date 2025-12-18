"""
QUESTION:
Write a function `wordSubsets(A, B)` that takes two lists of words `A` and `B` as input, where each word is composed of lowercase letters. The function should return a list of words from `A` that are universal, meaning every word in `B` is a subset of these words. A word `b` is a subset of word `a` if all letters in `b` are present in `a`, taking into account their frequency. The order of words in the output list is arbitrary.

The input lists `A` and `B` have the following constraints: `1 <= len(A), len(B) <= 10000`, `1 <= len(A[i]), len(B[i]) <= 10`, and all words in `A` are unique.
"""

def wordSubsets(A, B):
    maxB = [0]*26
    for b in B:
        for i, c in enumerate([b.count(chr(97+i)) for i in range(26)]):
            maxB[i] = max(maxB[i], c)
            
    res = []
    for a in A:
        cnts = [a.count(chr(97+i)) for i in range(26)]
        if all(b <= a for a, b in zip(cnts, maxB)):
            res.append(a)

    return res