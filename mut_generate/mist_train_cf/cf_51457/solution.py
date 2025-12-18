"""
QUESTION:
Implement a function `BurrowsWheelerTransform(string)` that takes a string as input, generates all its circular permutations, sorts them, and returns the string formed by the last character of each permutation. The input string only contains lowercase letters and its length is a multiple of the length of its substring that repeats.
"""

def BurrowsWheelerTransform(string):
    n = len(string)
    permutations = [string[i:n] + string[0:i] for i in range(n)]
    permutations.sort()
    bwt = ''.join([perm[-1] for perm in permutations])
    return bwt