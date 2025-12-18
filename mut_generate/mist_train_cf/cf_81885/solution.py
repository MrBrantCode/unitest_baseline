"""
QUESTION:
Create a function `distinct_permutations` that takes an ASCII input string and an integer `n` as parameters. The function should return `n` distinct permutations of the characters in the string, without repetition of the same permutation. If `n` is larger than the total number of distinct permutations, return all distinct permutations. The function should handle strings of any length, but note that efficiency may be a concern for long strings due to the factorial growth of permutations.
"""

from itertools import permutations 

def distinct_permutations(string, n):
    perms = list(permutations(string))
    perms = list(set(perms))
    
    if n > len(perms):
        return [''.join(p) for p in perms]
    else:
        return [''.join(perms[i]) for i in range(n)]